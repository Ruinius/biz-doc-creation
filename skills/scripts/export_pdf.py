import sys
import markdown
from xhtml2pdf import pisa

def export_to_pdf(markdown_path, pdf_path):
    with open(markdown_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # Convert markdown to html
    html_content = markdown.markdown(md_text, extensions=['extra'])

    # Wrap in basic HTML structure and apply beautiful styling
    html_string = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Document</title>
        <style>
            @page {{
                size: a4;
                margin: 2cm;
            }}
            body {{
                font-family: Helvetica, Arial, sans-serif;
                line-height: 1.5;
                color: #333;
                font-size: 11pt;
            }}
            h1 {{
                font-size: 20pt;
                color: #2c3e50;
                border-bottom: 1px solid #3498db;
                padding-bottom: 8px;
                margin-bottom: 15px;
                font-weight: normal;
            }}
            h2 {{
                font-size: 14pt;
                color: #2c3e50;
                margin-top: 20px;
                margin-bottom: 10px;
                font-weight: bold;
            }}
            p {{
                margin-bottom: 12px;
                text-align: justify;
            }}
            ul {{
                margin-bottom: 12px;
            }}
            li {{
                margin-bottom: 4px;
            }}
            strong {{
                font-weight: bold;
                color: #1a252f;
            }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    with open(pdf_path, "wb") as result_file:
        pisa_status = pisa.CreatePDF(html_string, dest=result_file)

    if pisa_status.err:
        print(f"Error creating PDF: {pisa_status.err}")
        sys.exit(1)
    else:
        print(f"Successfully created {pdf_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python export_pdf.py <input.md> <output.pdf>")
        sys.exit(1)
    
    export_to_pdf(sys.argv[1], sys.argv[2])
