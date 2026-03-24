import argparse
import os
import pandas as pd
from datapizza.clients.openai_like import OpenAILikeClient
from datapizza.agents import Agent

# ==========================================
# VARIABILI COSTANTI (Configurazione)
# ==========================================
JWT_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijc3MzRiNDA1LTYyNDYtNDY0ZS04ZDcxLWVlNzFlZDM4ZmM0MSIsImV4cCI6MTc3NTgzNzE2MSwianRpIjoiM2Y3YmVlZTAtYzcyMy00N2E3LWJmZWQtMTUwNTViZjU2ZTdmIn0.NZPAlmGRGzBzCocP6w48V4V0QoukZb_abA1f9KmNzjQ"         # Inserisci il tuo token di Open WebUI
RAG_MODEL = "subset40-expertnemotronsuper"             # Inserisci l'ID esatto del modello (senza parentesi)
BASE_URL = "http://localhost/api/v1"       # URL base delle API

def main():
    parser = argparse.ArgumentParser(description="Pipeline RAG Semplificata (Solo Generazione).")
    parser.add_argument("--input", required=True, help="Percorso del file Excel/CSV di input")
    parser.add_argument("--output", default="risultati_rag_finali.xlsx", help="Percorso del file Excel di output")
    args = parser.parse_args()

    # 1. Configurazione Client RAG (usando le costanti in alto)
    client_rag = OpenAILikeClient(
        api_key=JWT_TOKEN, 
        model=RAG_MODEL,
        base_url=BASE_URL 
    )

    # 2. Inizializzazione Agente
    agente_rag = Agent(
        name="generatore-rag",
        client=client_rag,
        system_prompt="""Sei un assistente esperto in normative.
Rispondi alla domanda in modo preciso basandoti SOLO sul contesto fornito.

REGOLA FONDAMENTALE: Struttura SEMPRE la tua risposta in questo esatto modo:
1. Risposta: [La tua risposta discorsiva in italiano]
2. Testo Originale: "[Copia-incolla esatto del paragrafo del contesto su cui ti basi]"

Se l'informazione non è presente, scrivi solo "INFORMAZIONE NON PRESENTE"."""
    )

    # 3. Lettura del file di input
    print(f"Lettura del file: {args.input}")
    try:
        if args.input.lower().endswith('.csv'):
            df = pd.read_csv(args.input)
        else:
            df = pd.read_excel(args.input)
    except Exception as e:
        print(f"❌ Errore nella lettura del file: {e}")
        return

    colonna_domanda = df.columns[0]

    # ==========================================
    # FASE UNICA: Generazione RAG
    # ==========================================
    print("\n" + "=" * 50)
    print(f"Inizio Generazione con modello: {RAG_MODEL}")
    print("=" * 50)
    
    risposte_rag = []
    fonti_estratte = []
    
    for index, row in df.iterrows():
        domanda = str(row[colonna_domanda])
        print(f"[{index + 1}/{len(df)}] Genero risposta per: {domanda[:40]}...")
        
        try:
            risultato = agente_rag.run(domanda).text
            
            # Divisione della stringa per popolare due colonne separate
            if "2. Testo Originale:" in risultato:
                parti = risultato.split("2. Testo Originale:")
                risposte_rag.append(parti[0].replace("1. Risposta:", "").strip())
                fonti_estratte.append(parti[1].strip())
            else:
                # Se il modello non segue il formato per qualche motivo
                risposte_rag.append(risultato.strip())
                fonti_estratte.append("Fonte non formattata correttamente")
                
        except Exception as e:
            print(f"  ⚠️ Errore durante la generazione: {e}")
            risposte_rag.append("ERRORE GENERAZIONE")
            fonti_estratte.append("ERRORE GENERAZIONE")

    # 4. Salvataggio ed Esportazione
    df['Risposta RAG'] = risposte_rag
    df['Paragrafo Fonte RAG'] = fonti_estratte
    
    try:
        df.to_excel(args.output, index=False)
        print("\n" + "=" * 50)
        print(f"✅ Processo completato! File salvato in: {args.output}")
    except Exception as e:
        print(f"\n❌ Errore durante il salvataggio finale: {e}")

if __name__ == "__main__":
    main()