import sys
import re
from docx import Document
from docx.shared import Pt, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH

def process_bold_text(paragraph, text):
    """Splits text by ** and alternates adding normal and bold runs."""
    parts = re.split(r'\*\*(.*?)\*\*', text)
    for i, part in enumerate(parts):
        if not part:
            continue
        run = paragraph.add_run(part)
        if i % 2 == 1:
            run.bold = True

def export_to_docx(markdown_path, docx_path):
    doc = Document()
    
    # Optional: Customize default styles for a "beautiful" look
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = Pt(11)
    
    # Heading 1 style
    h1_style = doc.styles['Heading 1']
    h1_style.font.name = 'Arial'
    h1_style.font.size = Pt(20)
    h1_style.font.bold = False
    
    # Heading 2 style
    h2_style = doc.styles['Heading 2']
    h2_style.font.name = 'Arial'
    h2_style.font.size = Pt(14)
    
    with open(markdown_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        line_stripped = line.rstrip()
        if not line_stripped:
            continue
            
        leading_spaces = len(line) - len(line.lstrip())
        content = line.strip()

        if content.startswith('# '):
            p = doc.add_heading(level=1)
            process_bold_text(p, content[2:])
        elif content.startswith('## '):
            p = doc.add_heading(level=2)
            process_bold_text(p, content[3:])
        elif content.startswith('- ') or content.startswith('* '):
            level = leading_spaces // 2
            style_name = 'List Bullet' if level == 0 else f'List Bullet {level + 1}'
            try:
                p = doc.add_paragraph(style=style_name)
            except KeyError:
                # Fallback if style doesn't exist
                p = doc.add_paragraph(style='List Bullet')
            process_bold_text(p, content[2:])
        else:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
            process_bold_text(p, content)

    doc.save(docx_path)
    print(f"Successfully created {docx_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python export_docx.py <input.md> <output.docx>")
        sys.exit(1)
    
    export_to_docx(sys.argv[1], sys.argv[2])
