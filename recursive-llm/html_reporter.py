"""
html_reporter.py — Genera un report HTML con link cliccabili al PDF annotato.

Ogni citazione [¶N] nella risposta diventa un link che apre
annotated_bboxes.pdf alla pagina corrispondente con le bounding box.
"""

import os
import re
from pathlib import Path
from typing import Any


def _linkify_anchors(text: str, anchor_page: dict[str, int], pdf_path: str,
                     single_pdf_path: str | None = None,
                     anchor_single_page: dict[str, int] | None = None) -> str:
    """Sostituisce [¶N] con link al PDF single-bbox (se disponibile) o a quello completo."""

    def replacer(m: re.Match) -> str:
        anchor = f"¶{m.group(1)}"
        # Preferisci il PDF con bbox singola se disponibile per questo anchor
        if single_pdf_path and anchor_single_page and anchor in anchor_single_page:
            spage = anchor_single_page[anchor]
            return (
                f'<a href="{single_pdf_path}#page={spage}" '
                f'title="Apri PDF con solo questa citazione evidenziata" '
                f'target="_blank" class="citation single-bbox">[{anchor}]</a>'
            )
        page = anchor_page.get(anchor)
        if page is None:
            return m.group(0)
        return (
            f'<a href="{pdf_path}#page={page}" '
            f'title="Apri PDF a pagina {page} (tutte le bbox)" '
            f'target="_blank" class="citation">[{anchor}]</a>'
        )

    return re.sub(r"\[¶(\d+)\]", replacer, text)


def generate_html_report(
    results: list[dict[str, Any]],
    doc_dir: str,
    output_path: str,
    model: str = "",
    title: str = "Report Q&A con Fonti",
) -> Path:
    """Genera un report HTML con risposte e link cliccabili alle fonti.

    Args:
        results: lista di {
            question, expected_answer, expected_page, answer, sources
        }
        sources è lista di {anchor, page, type, content}
        doc_dir: cartella che contiene annotated_bboxes.pdf
        output_path: dove salvare l'HTML
        model: nome del modello usato
        title: titolo del report
    """
    doc_dir_path = Path(doc_dir)
    pdf_absolute = (doc_dir_path / "annotated_bboxes.pdf").resolve()
    single_pdf_absolute = (doc_dir_path / "annotated_bboxes_single.pdf").resolve()
    html_dir = Path(output_path).parent.resolve()

    pdf_rel = os.path.relpath(str(pdf_absolute), str(html_dir))
    single_pdf_rel = os.path.relpath(str(single_pdf_absolute), str(html_dir)) if single_pdf_absolute.exists() else None

    rows_html: list[str] = []

    for i, r in enumerate(results, 1):
        question = r.get("question", "")
        expected_answer = r.get("expected_answer") or ""
        expected_page = r.get("expected_page") or ""
        answer = r.get("answer", "")
        sources: list[dict] = r.get("sources", [])

        # Mappa anchor → pagina per linkify
        anchor_page: dict[str, int] = {
            s["anchor"]: s["page"] for s in sources
        }
        anchor_single_page: dict[str, int] = {
            s["anchor"]: s["single_pdf_page"] for s in sources if "single_pdf_page" in s
        }

        # Trasforma [¶N] in link cliccabili nella risposta
        answer_linked = _linkify_anchors(answer, anchor_page, pdf_rel,
                                         single_pdf_rel, anchor_single_page)

        # Colonna Fonti
        if sources:
            fonti_parts = []
            for s in sources:
                a = s["anchor"]
                p = s["page"]
                if single_pdf_rel and "single_pdf_page" in s:
                    href = f"{single_pdf_rel}#page={s['single_pdf_page']}"
                    title = "PDF con solo questa citazione evidenziata"
                    cls = "source-link single-bbox"
                else:
                    href = f"{pdf_rel}#page={p}"
                    title = "Apri PDF a pagina"
                    cls = "source-link"
                fonti_parts.append(
                    f'<a href="{href}" target="_blank" '
                    f'class="{cls}" title="{title}">{a}</a>'
                    f'<span class="source-page">(p. {p})</span>'
                )
            fonti_html = " ".join(fonti_parts)
        else:
            fonti_html = '<span class="no-source">—</span>'

        rows_html.append(f"""
            <tr>
                <td class="col-num">{i}</td>
                <td class="col-question">{question}</td>
                <td class="col-gt">{expected_answer}</td>
                <td class="col-gt-page">{expected_page}</td>
                <td class="col-answer">{answer_linked}</td>
                <td class="col-sources">{fonti_html}</td>
            </tr>
        """)

    style = """
    <style>
        :root {
            --bg: #f5f5f5;
            --card-bg: #ffffff;
            --text: #333333;
            --muted: #777777;
            --accent: #2563eb;
            --accent-hover: #1d4ed8;
            --border: #e5e5e5;
            --header-bg: #1e293b;
            --header-text: #ffffff;
            --gt-bg: #f0fdf4;
            --num-color: #94a3b8;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
            margin: 0; padding: 24px;
            background: var(--bg); color: var(--text);
            line-height: 1.6;
        }
        .container { max-width: 1400px; margin: 0 auto; }
        h1 { text-align: center; color: #1e293b; margin-bottom: 8px; font-size: 1.5em; }
        .meta {
            text-align: center; color: var(--muted); margin-bottom: 24px;
            font-size: 0.9em;
        }
        .table-wrapper {
            background: var(--card-bg); border-radius: 12px;
            box-shadow: 0 2px 12px rgba(0,0,0,0.06); overflow: hidden;
        }
        table {
            width: 100%; border-collapse: collapse; font-size: 0.92em;
            table-layout: fixed;
        }
        th, td {
            padding: 14px 16px; border-bottom: 1px solid var(--border);
            vertical-align: top; word-wrap: break-word;
        }
        th {
            background: var(--header-bg); color: var(--header-text);
            font-weight: 600; font-size: 0.85em; text-transform: uppercase;
            letter-spacing: 0.4px; text-align: left; position: sticky; top: 0; z-index: 1;
        }
        th.col-num      { width: 3%;  text-align: center; }
        th.col-question { width: 17%; }
        th.col-gt       { width: 20%; background: #166534; }
        th.col-gt-page  { width: 5%;  text-align: center; background: #166534; }
        th.col-answer   { width: 38%; background: #0f3b5c; }
        th.col-sources  { width: 17%; }

        td.col-num { text-align: center; color: var(--num-color); font-weight: 600; }
        td.col-gt { background: var(--gt-bg); font-size: 0.88em; }
        td.col-gt-page { background: var(--gt-bg); text-align: center; font-weight: 600; }
        td.col-answer { line-height: 1.7; }

        tr:hover td { background: #fafbfc; }
        tr:hover td.col-gt { background: #e6f7ec; }

        /* Stili citazioni */
        a.citation {
            color: var(--accent); text-decoration: none; font-weight: 600;
            font-size: 0.85em; padding: 1px 4px; border-radius: 3px;
            background: #eff6ff; white-space: nowrap;
            transition: background 0.15s, color 0.15s;
        }
        a.citation:hover { background: #dbeafe; color: var(--accent-hover); }
        a.citation.single-bbox {
            border-left: 2px solid #16a34a; padding-left: 3px;
        }

        /* Stili fonti */
        a.source-link {
            display: inline-block; color: var(--accent); text-decoration: none;
            font-weight: 600; padding: 2px 6px; border-radius: 3px;
            background: #eff6ff; margin: 2px 1px; font-size: 0.9em;
            transition: background 0.15s;
        }
        a.source-link:hover { background: #dbeafe; }
        a.source-link.single-bbox {
            border-left: 2px solid #16a34a; padding-left: 4px;
        }
        .source-page { font-size: 0.8em; color: var(--muted); margin-left: 2px; }
        .no-source { color: var(--muted); font-style: italic; }

        /* Markdown rendering interno */
        td.col-answer p { margin-bottom: 8px; }
        td.col-answer ul, td.col-answer ol { margin: 6px 0 6px 20px; }
        td.col-answer li { margin-bottom: 4px; }
        td.col-answer table { width: 100%; border-collapse: collapse; margin: 8px 0; font-size: 0.85em; }
        td.col-answer th, td.col-answer td { border: 1px solid #d1d5db; padding: 6px 8px; }
        td.col-answer code { background: #f1f5f9; padding: 1px 4px; border-radius: 3px; font-size: 0.9em; }
        td.col-answer pre { background: #1e293b; color: #e2e8f0; padding: 12px; border-radius: 6px; overflow-x: auto; font-size: 0.85em; }
        td.col-answer strong { font-weight: 600; color: #1e293b; }

        @media (max-width: 1024px) {
            table { font-size: 0.82em; }
            th, td { padding: 10px 8px; }
        }
    </style>
    """

    model_info = f"Modello: {model}" if model else ""
    pdf_desc = "PDF con bbox singola per citazione" if single_pdf_rel else "PDF annotato con bounding box"

    full_html = f"""<!DOCTYPE html>
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
    {style}
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        <div class="meta">
            {model_info}
            {' · ' if model_info else ''}
            {len(results)} domande · {pdf_desc}
        </div>
        <div class="table-wrapper">
            <table>
                <thead>
                    <tr>
                        <th class="col-num">#</th>
                        <th class="col-question">Domanda</th>
                        <th class="col-gt">Risposta Attesa</th>
                        <th class="col-gt-page">Pag.</th>
                        <th class="col-answer">Risposta Modello</th>
                        <th class="col-sources">Fonti</th>
                    </tr>
                </thead>
                <tbody>
                    {"".join(rows_html)}
                </tbody>
            </table>
        </div>
    </div>
    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            marked.use({{ breaks: true }});
            const answerCells = document.querySelectorAll('td.col-answer');
            answerCells.forEach(cell => {{
                let html = cell.innerHTML;
                // Estrai le citation link gia' generate e sostituiscile con placeholder
                const citations = [];
                html = html.replace(/<a class="citation"[^>]*>.*?<\\/a>/g, match => {{
                    citations.push(match);
                    return '%%CITATION' + (citations.length - 1) + '%%';
                }});
                // Render markdown sul resto
                let rendered = marked.parse(html);
                // Rimetti le citation link al loro posto
                citations.forEach((cit, idx) => {{
                    rendered = rendered.replace('%%CITATION' + idx + '%%', cit);
                }});
                cell.innerHTML = rendered;
            }});
        }});
    </script>
</body>
</html>
"""

    out = Path(output_path)
    out.write_text(full_html, encoding="utf-8")
    return out
