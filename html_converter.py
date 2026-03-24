import argparse
import os
import pandas as pd

def esporta_in_html(input_file, output_file):
    print(f"Lettura del file: {input_file}...")
    
    # Supporto per leggere sia Excel che CSV
    try:
        if input_file.lower().endswith('.csv'):
            df = pd.read_csv(input_file)
        else:
            df = pd.read_excel(input_file)
    except Exception as e:
        print(f"❌ Errore nella lettura del file: {e}")
        return

    print("Generazione del report HTML in corso...")

    # Template HTML e CSS moderno
    html_template = """
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Report Risposte RAG</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&display=swap');
            
            body { font-family: 'Inter', sans-serif; background-color: #f4f7f8; color: #333; margin: 0; padding: 40px 20px; }
            h1 { text-align: center; color: #1e293b; margin-bottom: 40px; font-weight: 700; letter-spacing: -0.5px; }
            .container { max-width: 1500px; margin: 0 auto; background-color: #fff; border-radius: 12px; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1); overflow: hidden; }
            table { width: 100%; border-collapse: collapse; text-align: left; table-layout: fixed; }
            th, td { padding: 20px; border-bottom: 1px solid #e2e8f0; vertical-align: top; line-height: 1.6; word-wrap: break-word; }
            th { background-color: #f8fafc; color: #475569; font-weight: 600; text-transform: uppercase; font-size: 13px; letter-spacing: 0.5px; }
            tr:last-child td { border-bottom: none; }
            tr:hover { background-color: #fbfcfd; }
            
            /* Stili per le colonne (Totale 100%) */
            .col-domanda { width: 15%; font-weight: 600; color: #0f172a; }
            .col-verita { width: 20%; color: #475569; font-size: 14px; background-color: #fafafa;}
            .col-pagina { width: 5%; text-align: center; font-weight: bold; color: #64748b; }
            .col-rag { width: 25%; font-size: 15px; color: #1e293b; background-color: #f0fdf4; }
            .col-fonte { width: 35%; font-size: 13px; color: #475569; font-style: italic; background-color: #f8fafc; border-left: 2px solid #cbd5e1; }
            
            /* Sfumatura per righe alternate */
            tbody tr:nth-child(even) { background-color: #fcfcfc; }
        </style>
    </head>
    <body>
        <h1>📊 Report Modello RAG (Fonti Estratte)</h1>
        <div class="container">
            <table>
                <thead>
                    <tr>
                        <th class="col-domanda">Domanda</th>
                        <th class="col-verita">Ground Truth Originale</th>
                        <th class="col-pagina">Pag.</th>
                        <th class="col-rag">Risposta Generata (RAG)</th>
                        <th class="col-fonte">Testo Originale (Fonte Citata)</th>
                    </tr>
                </thead>
                <tbody>
    """

    for index, row in df.iterrows():
        # Estrazione sicura delle colonne (0: Domanda, 1: Verità, 2: Pagina, 3: Risposta, 4: Fonte)
        domanda = str(row.iloc[0]).replace('\n', '<br>') if len(row) > 0 else "-"
        verita = str(row.iloc[1]).replace('\n', '<br>') if len(row) > 1 else "-"
        pagina = str(row.iloc[2]) if len(row) > 2 else "-"
        risposta_rag = str(row.iloc[3]).replace('\n', '<br>') if len(row) > 3 else "-"
        fonte_rag = str(row.iloc[4]).replace('\n', '<br>') if len(row) > 4 else "-"

        # Gestione di valori "nan" qualora una cella fosse vuota nell'Excel
        if "nan" == fonte_rag.lower(): fonte_rag = "Nessuna fonte citata"

        html_template += f"""
                    <tr>
                        <td class="col-domanda">{domanda}</td>
                        <td class="col-verita">{verita}</td>
                        <td class="col-pagina">{pagina}</td>
                        <td class="col-rag">{risposta_rag}</td>
                        <td class="col-fonte">"{fonte_rag}"</td>
                    </tr>
        """

    html_template += """
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """

    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(html_template)
        print(f"✅ Fatto! Report HTML generato con successo in: {output_file}")
    except Exception as e:
        print(f"❌ Errore durante il salvataggio del file HTML: {e}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convertitore da Excel/CSV RAG a Report HTML")
    parser.add_argument("--input", required=True, help="Il file Excel o CSV con i risultati (es. risultati_rag_finali.xlsx)")
    
    args = parser.parse_args()
    
    if not os.path.exists(args.input):
        print(f"❌ Errore: Il file {args.input} non esiste in questa cartella.")
    else:
        # Estrapola il nome senza estensione e aggiunge .html
        nome_base = os.path.splitext(args.input)[0]
        file_output = f"{nome_base}.html"
        
        esporta_in_html(args.input, file_output)