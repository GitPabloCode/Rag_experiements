"""Script per estrarre risposte da un file Markdown basato su domande in un file Excel."""

import argparse
import pandas as pd
from rlm import RLM

def main():
    # Configurazione dei parametri da riga di comando
    parser = argparse.ArgumentParser(description="Estrae dati usando RLM partendo da un Markdown e un file Excel di domande.")
    parser.add_argument("--md_file", required=True, help="Percorso del file Markdown di input contenente il testo.")
    parser.add_argument("--excel_in", required=True, help="Percorso del file Excel/CSV contenente le domande.")
    parser.add_argument("--excel_out", default="risposte_subset_26_35_40_58.xlsx", help="Percorso del file Excel di output da generare.")
    args = parser.parse_args()

    # 1. Lettura del file Markdown
    print(f"📄 Lettura del file Markdown: {args.md_file}...")
    try:
        with open(args.md_file, "r", encoding="utf-8") as f:
            document = f.read()
    except Exception as e:
        print(f"❌ Errore nella lettura del file Markdown: {e}")
        return

    # 2. Lettura del file con le domande (supporta sia CSV che Excel)
    print(f"📊 Lettura delle domande da: {args.excel_in}...")
    try:
        if args.excel_in.endswith('.csv'):
            df_input = pd.read_csv(args.excel_in)
        else:
            df_input = pd.read_excel(args.excel_in)
            
        # Assicuriamoci che esista la colonna 'Domanda'
        if 'Domanda' not in df_input.columns:
            raise ValueError("Il file di input non contiene una colonna chiamata 'Domanda'.")
            
        # Estrai la lista delle domande (rimuovendo eventuali valori nulli/NaN)
        tasks = df_input['Domanda'].dropna().tolist()
        print(f"✅ Trovate {len(tasks)} domande da elaborare.")
        
    except Exception as e:
        print(f"❌ Errore nella lettura del file delle domande: {e}")
        return

    # 3. Inizializzazione del modello RLM
    print("\n🤖 Inizializzazione del modello RLM...")
    rlm = RLM(
        model="ollama/minimax-m2.7:cloud",
        max_iterations=15,
        temperature=0.3
    )

    # 4. Ciclo sequenziale sulle domande per generare le risposte
    risultati = []
    print("\n⏳ Inizio elaborazione...\n" + "=" * 80)
    
    for i, task in enumerate(tasks, 1):
        print(f"\nDomanda {i}/{len(tasks)}: {task}")
        print("-" * 80)
        
        try:
            # Esecuzione del modello sul testo markdown
            result = rlm.complete(task, document)
            print(f"Risposta Generata:\n{result}")
        except Exception as e:
            result = f"ERRORE GENERAZIONE: {e}"
            print(f"❌ {result}")
            
        # Salva la coppia domanda-risposta
        risultati.append({
            "Domanda": task,
            "Risposta Modello": result
        })

    # 5. Generazione del file Excel di output
    print("\n" + "=" * 80)
    print(f"💾 Salvataggio dei risultati in: {args.excel_out}...")
    try:
        df_output = pd.DataFrame(risultati)
        df_output.to_excel(args.excel_out, index=False)
        print("✅ Salvataggio completato con successo!")
    except Exception as e:
        print(f"❌ Errore nel salvataggio del file Excel: {e}")

if __name__ == "__main__":
    main()