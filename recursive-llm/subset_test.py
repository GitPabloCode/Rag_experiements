"""
Script RLM Pipeline (Datapizza Native).
"""

import argparse
import pandas as pd
import time
from pathlib import Path
from rlm import RLM

# Generatore HTML
from html_reporter import crea_report_html_semplificato

# ── Monitoraggio Tempo ────────────────────────────────────────────────────────
class StepTimer:
    def __init__(self):
        self.elapsed = 0.0
    def __enter__(self):
        self.start_time = time.perf_counter()
        return self
    def __exit__(self, *args):
        self.elapsed = time.perf_counter() - self.start_time

# ── Esecuzione ────────────────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Esecuzione RLM nativa Datapizza.")
    parser.add_argument("--md_file", required=True)
    parser.add_argument("--excel_in", required=True)
    parser.add_argument("--parti_da", type=int, default=1)
    args = parser.parse_args()

    input_path = Path(args.excel_in)

    print(f"📄 Lettura del file Markdown: {args.md_file}...")
    try:
        with open(args.md_file, "r", encoding="utf-8") as f:
            document = f.read()
    except Exception as e:
        print(f"❌ Errore lettura Markdown: {e}"); return

    print(f"📊 Lettura delle domande...")
    df_input = pd.read_csv(args.excel_in) if input_path.suffix == '.csv' else pd.read_excel(args.excel_in)
    df_input = df_input.dropna(subset=['Domanda'])
    tasks_data = df_input.to_dict('records')

    start_index = max(1, args.parti_da)
    if start_index > 1:
        tasks_data = tasks_data[start_index - 1:]

    # Inizializza RLM (Ora usa Datapizza di nascosto!)
    print("\n🤖 Inizializzazione RLM (Datapizza Engine)...")
    rlm = RLM(
        model="qwen3.5:cloud",
        recursive_model="qwen3.5:4b",
        api_base="http://localhost:11434/v1",
        max_iterations=60
    )

    risultati = []
    global_start = time.perf_counter()
    totale_token_script = 0

    print("\n⏳ Inizio elaborazione...\n" + "=" * 60)

    for i, row in enumerate(tasks_data, start=start_index):
        task = row['Domanda']
        gt = row.get('Risposta', row.get('Ground_Truth', ''))

        print(f"\nDomanda {i}/{len(df_input)}: {task}")
        print("-" * 60)

        with StepTimer() as timer:
            # Eseguiamo il modello
            answer = rlm.complete(task, document)

            # Estraiamo i token comodamente dalle statistiche!
            step_tokens = rlm.stats['total_tokens']
            totale_token_script += step_tokens

        print(f"Risposta Generata:\n{answer}")
        print("-" * 60)
        print(f" > Tempo: {timer.elapsed:.2f}s | Token: {step_tokens}")

        risultati.append({
            "Domanda": task,
            "Ground_Truth": gt,
            "Risposta_Modello": answer,
            "Tempo_s": round(timer.elapsed, 2),
            "Token": step_tokens
        })

    global_time = time.perf_counter() - global_start

    # Salvataggio
    output_dir = Path("risposte_rlm")
    output_dir.mkdir(parents=True, exist_ok=True)

    df_output = pd.DataFrame(risultati)
    df_output.to_excel(output_dir / f"{input_path.stem}_rlm_output.xlsx", index=False)
    crea_report_html_semplificato(df_output, str(output_dir / f"{input_path.stem}_rlm_report.html"))

    print("\n" + "=" * 60)
    print(f"✅ COMPLETATO | Tempo Tot: {global_time:.2f}s | Token Tot: {totale_token_script}")

if __name__ == "__main__":
    main()