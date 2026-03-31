"""Script per estrarre risposte da un file Markdown basato su domande in un file Excel."""

import argparse
import pandas as pd
from rlm import RLM

def main():
    # Configurazione dei parametri da riga di comando
    parser = argparse.ArgumentParser(description="Estrae dati usando RLM partendo da un Markdown e un file Excel di domande.")
    parser.add_argument("--md_file", required=True, help="Percorso del file Markdown di input contenente il testo.")
    parser.add_argument("--excel_in", required=True, help="Percorso del file Excel/CSV contenente le domande e la Ground Truth.")
    parser.add_argument("--excel_out", default="risposte_modello.xlsx", help="Percorso del file Excel di output da generare.")
    # NUOVO PARAMETRO: --parti_da
    parser.add_argument("--parti_da", type=int, default=1, help="Indice della domanda da cui partire (es. 3 per partire dalla terza domanda). Default: 1.")
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
            
        # Rimuoviamo righe in cui la domanda è vuota
        df_input = df_input.dropna(subset=['Domanda'])
        # Convertiamo il dataframe in una lista di dizionari per iterare facilmente
        tasks_data = df_input.to_dict('records')
        totale_domande = len(tasks_data)
        print(f"✅ Trovate {totale_domande} domande nel file.")
        
    except Exception as e:
        print(f"❌ Errore nella lettura del file delle domande: {e}")
        return

    # LOGICA DI FILTRAGGIO IN BASE A --parti_da
    start_index = max(1, args.parti_da) # Evita numeri negativi o zero
    if start_index > 1:
        if start_index > totale_domande:
            print(f"⚠️ Attenzione: hai chiesto di partire dalla domanda {start_index}, ma ci sono solo {totale_domande} domande. Nessuna operazione eseguita.")
            return
        print(f"⏭️  Salto le prime {start_index - 1} domande. Partenza dalla domanda numero {start_index}.")
        # Tagliamo la lista per tenere solo le domande da start_index in poi (ricorda che le liste partono da 0)
        tasks_data = tasks_data[start_index - 1:]

    # 3. Inizializzazione del modello RLM
    print("\n🤖 Inizializzazione del modello RLM...")
    rlm = RLM(
        model="ollama/qwen3.5:9b",
        #recursive_model="ollama/gpt-oss:120b-cloud",
        max_iterations=50,
        temperature=0.3
    )

    # 4. Ciclo sequenziale sulle domande per generare le risposte
    risultati = []
    print("\n⏳ Inizio elaborazione...\n" + "=" * 80)
    
    # Usiamo start_index in enumerate così stampa il numero di domanda corretto rispetto al file originale
    for i, row in enumerate(tasks_data, start=start_index):
        task = row['Domanda']
        # Recuperiamo Risposta e Pagina (se non esistono nel file di input, mettiamo stringa vuota)
        gt_risposta = row.get('Risposta', '')
        pagina = row.get('Pagina', '')

        print(f"\nDomanda {i}/{totale_domande}: {task}")
        print("-" * 80)
        
        try:
            # Esecuzione del modello sul testo markdown
            result = rlm.complete(task, document)
            print(f"Risposta Generata:\n{result}")
        except Exception as e:
            result = f"ERRORE GENERAZIONE: {e}"
            print(f"❌ {result}")
            
        # Salva la riga completa per l'Excel finale
        risultati.append({
            "Domanda": task,
            "Risposta": gt_risposta,
            "Pagina": pagina,
            "Risposta Modello": result
        })

    # 5. Generazione del file Excel di output
    print("\n" + "=" * 80)
    print(f"💾 Salvataggio dei risultati in: {args.excel_out}...")
    try:
        # Il DataFrame creerà automaticamente le colonne nell'ordine in cui sono state inserite nel dizionario
        df_output = pd.DataFrame(risultati)
        df_output.to_excel(args.excel_out, index=False)
        print("✅ Salvataggio completato con successo!")
    except Exception as e:
        print(f"❌ Errore nel salvataggio del file Excel: {e}")

if __name__ == "__main__":
    main()