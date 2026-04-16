"""
Modulo per la generazione del report HTML dei risultati.
"""
import pandas as pd


def crea_report_html_semplificato(df: pd.DataFrame, output_file: str):
    """
    Crea il report HTML con il rendering Markdown e le metriche.
    """
    df_html = pd.DataFrame()
    df_html['Domanda'] = df['Domanda']
    df_html['Ground Truth'] = df['Ground_Truth']
    df_html['Risposta Modello'] = df['Risposta_Modello']
    df_html['Tempo (s)'] = df['Tempo_s']
    df_html['Token'] = df['Token']

    html_table = df_html.to_html(escape=False, index=False, classes='table')

    style = """
    <style>
        body { font-family: 'Segoe UI', Tahoma, sans-serif; margin: 20px; background-color: #f4f6f9; color: #333; }
        h1 { text-align: center; color: #2c3e50; margin-bottom: 20px; }
        .table-container { background: white; padding: 20px; border-radius: 10px; box-shadow: 0 4px 15px rgba(0,0,0,0.05); }
        table { width: 100%; border-collapse: collapse; font-size: 0.95em; table-layout: fixed; }
        th, td { padding: 15px; border-bottom: 1px solid #e9ecef; vertical-align: top; word-wrap: break-word; }
        th { background-color: #34495e; color: white; }

        /* Larghezze Colonne */
        th:nth-child(1) { width: 20%; } 
        th:nth-child(2) { width: 30%; background-color: #2c3e50; } 
        th:nth-child(3) { width: 35%; background-color: #1a252f; } 
        th:nth-child(4) { width: 7%; text-align: center; } 
        th:nth-child(5) { width: 8%; text-align: center; } 

        td:nth-child(4), td:nth-child(5) { text-align: center; vertical-align: middle; font-family: monospace; font-weight: bold; color: #d35400; }
        tr:hover { background-color: #f1f3f5; }

        /* Markdown Style */
        td:nth-child(3) { line-height: 1.6; }
        td:nth-child(3) p { margin-top: 0; margin-bottom: 10px; }
        td:nth-child(3) ul { margin-top: 5px; padding-left: 20px; }
        td:nth-child(3) table { width: 100%; border-collapse: collapse; font-size: 0.9em; }
        td:nth-child(3) th, td:nth-child(3) td { border: 1px solid #bdc3c7; padding: 8px; }
    </style>
    """

    full_html = f"""
    <!DOCTYPE html>
    <html lang="it">
    <head>
        <meta charset="UTF-8">
        <title>Report RLM Performance</title>
        <script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
        {style}
    </head>
    <body>
        <h1>Comparazione RLM: Testo Integrale</h1>
        <div class="table-container">{html_table}</div>
        <script>
            document.addEventListener("DOMContentLoaded", function() {{
                marked.use({{ breaks: true }});
                const rows = document.querySelectorAll('.table tbody tr');
                rows.forEach(row => {{
                    const cell = row.querySelector(`td:nth-child(3)`);
                    if (cell) {{
                        let rawText = cell.textContent || cell.innerText;
                        rawText = rawText.replace(/\\\\n/g, '\\n').replace(/\\\\r/g, '');
                        cell.innerHTML = marked.parse(rawText);
                    }}
                }});
            }});
        </script>
    </body>
    </html>
    """

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(full_html)