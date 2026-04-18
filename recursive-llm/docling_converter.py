#!/usr/bin/env python3
"""
convert_pdf.py - Converte un PDF in Markdown, JSON citabile e PDF annotato con bounding box.

Funzionalità:
  - Estrazione testo con layout preservato
  - Salvataggio immagini in images/ con riferimenti nel Markdown
  - Riconoscimento formule matematiche → LaTeX
  - JSON ibrido citabile: ogni paragrafo ha un ID univoco + metadati di provenienza
    (pagina, bbox, tipo elemento) → ideale per sistemi multi-agente con citazione della fonte
  - Visualizzazione bounding box per pagina unite in un unico PDF (senza frecce)
  - Range di pagine selezionabile
  - Warning HuggingFace/transformers soppressi

Installazione:
  pip install docling pillow fpdf2
  pip install docling[easyocr]   # opzionale: PDF scansionati

Utilizzo:
  python convert_pdf.py documento.pdf
  python convert_pdf.py documento.pdf --pages 1-5
  python convert_pdf.py documento.pdf --pages 1,3,5,7
  python convert_pdf.py documento.pdf --no-bbox-pdf
  python convert_pdf.py documento.pdf --no-math --no-images
  python convert_pdf.py documento.pdf --ocr
"""

# ── Soppressione warning HuggingFace/transformers ─────────────────────────────
import os
import warnings
os.environ["TOKENIZERS_PARALLELISM"] = "false"
warnings.filterwarnings("ignore", message=".*tie_word_embeddings.*")
warnings.filterwarnings("ignore", message=".*generation_config.*")
warnings.filterwarnings("ignore", message=".*Passing.*generation-related.*")
warnings.filterwarnings("ignore", category=UserWarning, module="transformers")
warnings.filterwarnings("ignore", category=FutureWarning, module="transformers")
# ─────────────────────────────────────────────────────────────────────────────

import argparse
import json
import sys
from pathlib import Path
from typing import Any

# ─── Label → colore RGB ──────────────────────────────────────────────────────
LABEL_COLORS: dict[str, tuple[int, int, int]] = {
    "title":          (220,  50,  50),
    "section_header": (220, 130,  30),
    "text":           ( 50, 120, 220),
    "list_item":      ( 50, 180, 100),
    "table":          (160,  60, 200),
    "picture":        ( 30, 180, 200),
    "formula":        (200,  80, 160),
    "code":           (100, 140,  30),
    "caption":        (180, 140,  60),
    "footnote":       (130, 130, 130),
    "page_header":    (180,  90,  90),
    "page_footer":    (180,  90,  90),
    "key_value":      ( 90, 160, 160),
}
DEFAULT_COLOR = (100, 100, 100)


# ─── Parsing argomenti ───────────────────────────────────────────────────────

def parse_pages(spec: str | None) -> set[int] | None:
    if spec is None:
        return None
    pages: set[int] = set()
    for part in spec.split(","):
        part = part.strip()
        if "-" in part:
            a, b = part.split("-", 1)
            pages.update(range(int(a), int(b) + 1))
        else:
            pages.add(int(part))
    return pages


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Converte un PDF in Markdown, JSON citabile e PDF annotato.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("pdf_path", type=str, help="Percorso al file PDF da convertire")
    parser.add_argument("--output-dir", type=str, default="processed_documents",
                        help="Cartella di output (default: processed_documents)")
    parser.add_argument("--pages", type=str, default=None,
                        help="Pagine da elaborare. Es: '1-5', '1,3,7', '2-4,8'")
    parser.add_argument("--no-images",   action="store_true", help="Senza estrazione immagini")
    parser.add_argument("--no-math",     action="store_true", help="Senza riconoscimento formule")
    parser.add_argument("--no-bbox-pdf", action="store_true", help="Senza PDF bounding box")
    parser.add_argument("--ocr",         action="store_true",
                        help="Forza OCR (PDF scansionati). Richiede: pip install docling[easyocr]")
    return parser.parse_args()


def check_dependencies() -> None:
    missing = []
    for pkg, install in [("docling", "docling"), ("PIL", "pillow"), ("fpdf", "fpdf2")]:
        try:
            __import__("PIL.Image" if pkg == "PIL" else pkg)
        except ImportError:
            missing.append(install)
    if missing:
        print("❌ Pacchetti mancanti. Installa con:")
        for m in missing:
            print(f"   pip install {m}")
        sys.exit(1)


# ─── Pipeline Docling ────────────────────────────────────────────────────────

def build_pipeline_options(extract_images: bool, extract_math: bool,
                            force_ocr: bool, need_page_images: bool):
    from docling.datamodel.pipeline_options import PdfPipelineOptions, TableFormerMode
    opts = PdfPipelineOptions()
    opts.do_table_structure = True
    opts.table_structure_options.mode = TableFormerMode.ACCURATE
    opts.generate_page_images    = need_page_images
    opts.generate_picture_images = extract_images
    opts.images_scale            = 2.0
    opts.do_formula_enrichment   = extract_math
    if force_ocr:
        try:
            from docling.datamodel.pipeline_options import EasyOcrOptions
            opts.do_ocr = True
            opts.ocr_options = EasyOcrOptions(force_full_page_ocr=True)
        except ImportError:
            print("⚠️  EasyOCR non trovato (pip install docling[easyocr]). OCR disabilitato.")
            opts.do_ocr = False
    else:
        opts.do_ocr = False
    return opts


def run_conversion(pdf_path: Path, extract_images: bool, extract_math: bool,
                   force_ocr: bool, need_page_images: bool):
    from docling.document_converter import DocumentConverter, PdfFormatOption
    from docling.datamodel.base_models import InputFormat
    opts = build_pipeline_options(extract_images, extract_math, force_ocr, need_page_images)
    converter = DocumentConverter(
        format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)}
    )
    return converter.convert(str(pdf_path))


# ─── JSON ibrido citabile ────────────────────────────────────────────────────




def _get_item_type(item) -> str:
    """Restituisce il tipo leggibile dell'item."""
    label = getattr(item, "label", None)
    if label is None:
        return type(item).__name__.lower().replace("item", "")
    return label.value if hasattr(label, "value") else str(label)


def build_hybrid_json(doc_result, pdf_path: Path,
                       page_filter: set[int] | None,
                       image_map: dict[str, str]) -> dict[str, Any]:
    """
    Costruisce il JSON ibrido snello per sistemi multi-agente.

    Struttura di ogni chunk:
    {
      "page_id":      3,            ← numero pagina (1-based)
      "paragraph_id": "p0042",      ← ID univoco del paragrafo (progressivo)
      "type":         "text",       ← text | section_header | title | list_item |
                                       table | formula | picture | code | caption | …
      "content":      "…markdown…"  ← contenuto in formato Markdown (quello che legge il modello)
    }
    """
    doc = doc_result.document
    chunks: list[dict[str, Any]] = []
    para_idx = 0

    for item, _level in doc.iterate_items():
        # Filtra per pagina se richiesto
        item_pages: set[int] = set()
        for prov in getattr(item, "prov", []):
            item_pages.add(prov.page_no)
        if page_filter and item_pages and not item_pages.intersection(page_filter):
            continue

        # Pagina di riferimento (prima occorrenza)
        page_id: int | None = None
        if hasattr(item, "prov") and item.prov:
            page_id = item.prov[0].page_no

        # Tipo elemento
        item_type = _get_item_type(item)

        # Contenuto in Markdown
        try:
            from docling_core.types.doc import TableItem as TI, PictureItem as PI
            if isinstance(item, TI):
                md_content = item.export_to_markdown()
            elif isinstance(item, PI):
                self_ref = getattr(item, "self_ref", "") or ""
                img_path = image_map.get(self_ref)
                captions = [
                    ann.text for ann in getattr(item, "annotations", [])
                    if getattr(ann, "text", None)
                ]
                caption_md = " ".join(captions)
                md_content = f"![{caption_md}]({img_path})" if img_path else f"[immagine: {caption_md}]"
            else:
                raw = getattr(item, "text", "") or ""
                # Formule: wrappa in LaTeX se il tipo è formula
                if item_type == "formula":
                    md_content = f"$$\n{raw}\n$$" if raw else "[formula]"
                # Intestazioni: aggiungi markdown heading
                elif item_type == "section_header":
                    lvl = getattr(item, "level", 1) or 1
                    md_content = f"{'#' * lvl} {raw}"
                elif item_type == "title":
                    md_content = f"# {raw}"
                elif item_type == "list_item":
                    md_content = f"- {raw}"
                elif item_type == "code":
                    lang = getattr(item, "code_language", "") or ""
                    md_content = f"```{lang}\n{raw}\n```"
                else:
                    md_content = raw
        except Exception:
            md_content = getattr(item, "text", "") or ""

        if not md_content.strip():
            continue  # salta elementi vuoti

        chunks.append({
            "page_id":      page_id,
            "paragraph_id": f"p{para_idx:04d}",
            "type":         item_type,
            "content":      md_content,
        })
        para_idx += 1

    return {
        "source_file": pdf_path.name,
        "total_pages": len(doc_result.document.pages),
        "total_chunks": len(chunks),
        "chunks": chunks,
    }


# ─── Immagini ────────────────────────────────────────────────────────────────

def save_images(doc_result, images_dir: Path) -> dict[str, str]:
    images_dir.mkdir(parents=True, exist_ok=True)
    image_map: dict[str, str] = {}
    for idx, picture in enumerate(doc_result.document.pictures, start=1):
        try:
            pil_image = picture.get_image(doc_result)
            if pil_image is None:
                continue
            fname = f"image_{idx:04d}.png"
            pil_image.save(str(images_dir / fname), format="PNG")
            ref = getattr(picture, "self_ref", None) or str(idx)
            image_map[ref] = f"images/{fname}"
            print(f"   🖼  {fname}")
        except Exception as e:
            print(f"   ⚠️  Immagine {idx}: {e}")
    return image_map


# ─── Export MD ───────────────────────────────────────────────────────────────

def export_markdown(doc_result, output_dir: Path, image_map: dict[str, str],
                    page_filter: set[int] | None) -> Path:
    md_text: str = doc_result.document.export_to_markdown()
    for ref_key, img_rel_path in image_map.items():
        alt = img_rel_path.replace("images/", "").replace(".png", "")
        md_img = f"![{alt}]({img_rel_path})"
        for ph in [f"<!-- image, {ref_key} -->", f"![]({ref_key})"]:
            md_text = md_text.replace(ph, md_img)
    if page_filter:
        pages_str = ", ".join(str(p) for p in sorted(page_filter))
        md_text = f"> ⚠️ Documento estratto dalle pagine: {pages_str}\n\n" + md_text
    md_path = output_dir / "document.md"
    md_path.write_text(md_text, encoding="utf-8")
    return md_path


# ─── Bounding box PDF ────────────────────────────────────────────────────────

def _get_label_color(label_str: str) -> tuple[int, int, int]:
    key = label_str.lower().replace(" ", "_").replace("-", "_")
    return LABEL_COLORS.get(key, DEFAULT_COLOR)


def draw_bboxes_on_page(doc_result, page_no: int):
    from PIL import Image, ImageDraw, ImageFont
    doc  = doc_result.document
    page = doc.pages.get(page_no)
    if page is None or page.image is None or page.image.pil_image is None:
        return None
    img: Image.Image = page.image.pil_image.copy().convert("RGB")
    draw = ImageDraw.Draw(img, "RGBA")
    page_h  = page.size.height
    page_w  = page.size.width
    img_w, img_h = img.size
    scale_x = img_w / page_w
    scale_y = img_h / page_h
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 13)
    except Exception:
        font = ImageFont.load_default()
    for item, _ in doc.iterate_items():
        if not hasattr(item, "prov") or not item.prov:
            continue
        for prov in item.prov:
            if prov.page_no != page_no:
                continue
            bbox = prov.bbox.to_top_left_origin(page_height=page_h)
            x0, y0 = bbox.l * scale_x, bbox.t * scale_y
            x1, y1 = bbox.r * scale_x, bbox.b * scale_y
            if x1 <= x0 or y1 <= y0:
                continue
            label_str = item.label.value if hasattr(item.label, "value") else str(item.label)
            r, g, b = _get_label_color(label_str)
            draw.rectangle([x0, y0, x1, y1], outline=(r, g, b, 230), width=2,
                           fill=(r, g, b, 30))
            label_short = label_str.replace("_", " ")
            try:
                tb = draw.textbbox((x0 + 2, y0 + 1), label_short, font=font)
                draw.rectangle(tb, fill=(r, g, b, 200))
                draw.text((x0 + 2, y0 + 1), label_short, fill=(255, 255, 255), font=font)
            except Exception:
                draw.text((x0 + 2, y0 + 1), label_short, fill=(r, g, b))
    return img


def build_bbox_pdf(doc_result, output_dir: Path, page_filter: set[int] | None) -> Path | None:
    try:
        from fpdf import FPDF
    except ImportError:
        print("   ⚠️  fpdf2 non trovato (pip install fpdf2). PDF bbox saltato.")
        return None
    doc   = doc_result.document
    pages = sorted(doc.pages.keys())
    pages_to_annotate = [p for p in pages if (page_filter is None or p in page_filter)]
    if not pages_to_annotate:
        return None
    bbox_dir = output_dir / "_bbox_tmp"
    bbox_dir.mkdir(exist_ok=True)
    pdf = FPDF(unit="pt")
    annotated_count = 0
    for page_no in pages_to_annotate:
        annotated = draw_bboxes_on_page(doc_result, page_no)
        if annotated is None:
            print(f"   ⚠️  Pagina {page_no}: immagine non disponibile, saltata.")
            continue
        tmp_path = bbox_dir / f"bbox_page_{page_no:04d}.png"
        annotated.save(str(tmp_path), format="PNG")
        page  = doc.pages[page_no]
        w_pt  = page.size.width
        h_pt  = page.size.height
        pdf.add_page(format=(w_pt, h_pt))
        pdf.image(str(tmp_path), x=0, y=0, w=w_pt, h=h_pt)
        annotated_count += 1
        print(f"   📄 Annotata pagina {page_no}")
    if annotated_count == 0:
        return None
    out_path = output_dir / "annotated_bboxes.pdf"
    pdf.output(str(out_path))
    for f in bbox_dir.glob("*.png"):
        f.unlink()
    bbox_dir.rmdir()
    return out_path


# ─── Main ────────────────────────────────────────────────────────────────────

def main() -> None:
    args = parse_args()
    check_dependencies()

    pdf_path = Path(args.pdf_path).expanduser().resolve()
    if not pdf_path.exists():
        print(f"❌ File non trovato: {pdf_path}")
        sys.exit(1)
    if pdf_path.suffix.lower() != ".pdf":
        print(f"❌ Il file non è un PDF: {pdf_path}")
        sys.exit(1)

    try:
        page_filter = parse_pages(args.pages)
    except Exception:
        print(f"❌ Formato pagine non valido: '{args.pages}'. Usa es. '1-5' o '1,3,7'.")
        sys.exit(1)

    output_dir = Path(args.output_dir) / pdf_path.stem
    output_dir.mkdir(parents=True, exist_ok=True)
    images_dir = output_dir / "images"

    extract_images = not args.no_images
    extract_math   = not args.no_math
    generate_bbox  = not args.no_bbox_pdf
    force_ocr      = args.ocr
    need_page_imgs = generate_bbox

    print(f"📁 Output in        : {output_dir}")
    if page_filter:
        print(f"📑 Pagine           : {', '.join(str(p) for p in sorted(page_filter))}")
    else:
        print(f"📑 Pagine           : tutte")
    print(f"🖼  Immagini         : {'✅' if extract_images else '❌'}")
    print(f"➕ Formule (LaTeX)   : {'✅' if extract_math else '❌'}")
    print(f"🔲 PDF bounding box  : {'✅' if generate_bbox else '❌'}")
    print(f"📋 JSON citabile     : ✅")
    print(f"🔍 OCR forzato       : {'✅' if force_ocr else '❌'}")
    print()

    # ── Conversione ───────────────────────────────────────────────────────────
    print("⚙️  Avvio conversione Docling...")
    try:
        doc_result = run_conversion(pdf_path, extract_images, extract_math,
                                    force_ocr, need_page_imgs)
    except Exception as e:
        print(f"❌ Errore conversione: {e}")
        raise

    # Escludi immagini di pagine fuori dal range per il PDF bbox
    if page_filter:
        doc = doc_result.document
        all_pages = set(doc.pages.keys())
        for pg in all_pages - page_filter:
            if pg in doc.pages and doc.pages[pg].image:
                doc.pages[pg].image = None

    # ── Immagini ──────────────────────────────────────────────────────────────
    image_map: dict[str, str] = {}
    if extract_images:
        print("\n🔍 Estrazione immagini di figura...")
        image_map = save_images(doc_result, images_dir)
        print(f"   Totale: {len(image_map)}")

    # ── Markdown ──────────────────────────────────────────────────────────────
    print("\n📝 Esportazione Markdown...")
    md_path = export_markdown(doc_result, output_dir, image_map, page_filter)
    print(f"   ✅ {md_path}")

    # ── JSON ibrido citabile ──────────────────────────────────────────────────
    print("\n🗂  Generazione JSON ibrido citabile...")
    hybrid = build_hybrid_json(doc_result, pdf_path, page_filter, image_map)
    json_path = output_dir / "document_citabile.json"
    json_path.write_text(json.dumps(hybrid, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"   ✅ {json_path}  ({hybrid['document']['num_chunks']} chunk)")

    # ── JSON raw Docling (legacy) ─────────────────────────────────────────────
    print("\n🗂  Esportazione JSON raw Docling...")
    try:
        raw_dict = doc_result.document.export_to_dict()
    except Exception:
        raw_dict = {}
    raw_json_path = output_dir / "document_raw.json"
    raw_json_path.write_text(json.dumps(raw_dict, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"   ✅ {raw_json_path}")

    # ── PDF bounding box ──────────────────────────────────────────────────────
    bbox_pdf_path: Path | None = None
    if generate_bbox:
        print("\n🔲 Generazione PDF con bounding box annotate...")
        bbox_pdf_path = build_bbox_pdf(doc_result, output_dir, page_filter)
        if bbox_pdf_path:
            print(f"   ✅ {bbox_pdf_path}")

    # ── Riepilogo ─────────────────────────────────────────────────────────────
    print("\n" + "=" * 60)
    print("✅ Conversione completata!")
    print(f"   📄 Markdown              : {md_path}")
    print(f"   📋 JSON citabile         : {json_path}  ({hybrid['total_chunks']} chunk)")
    print(f"   🗂  JSON raw Docling      : {raw_json_path}")
    if image_map:
        print(f"   🖼  Immagini             : {images_dir} ({len(image_map)} file)")
    if bbox_pdf_path:
        print(f"   🔲 PDF bbox annotato     : {bbox_pdf_path}")
    print("=" * 60)
    print()
    print("💡 Citazione agente:")
    print('   [fonte: paragraph_id="p0042", page_id=3, file="documento.pdf"]')


if __name__ == "__main__":
    main()