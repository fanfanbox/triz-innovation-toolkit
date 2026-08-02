#!/usr/bin/env python3
"""
TRIZ Report — Markdown to Word Converter (python-docx)
Generates professional Word documents with:
- Cover page (title + subtitle + author + date)
- 3-level TOC (update in Word after opening)
- Page breaks before H1 headings
- Table styling (blue header, alternating rows)
- Proper margins (2.54cm top/bottom, 3.18cm left/right)
"""

import argparse
import re
import sys
from pathlib import Path

from docx import Document
from docx.shared import Pt, Cm, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_ORIENT
from docx.oxml.ns import qn, nsdecls
from docx.oxml import parse_xml


def create_cover_page(doc, title, subtitle, author, date):
    """Create a professional cover page."""
    # Add blank paragraphs for spacing
    for _ in range(6):
        doc.add_paragraph()
    
    # Title
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(title)
    run.font.size = Pt(28)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 51, 102)  # Dark blue
    
    # Subtitle
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(subtitle)
    run.font.size = Pt(16)
    run.font.color.rgb = RGBColor(102, 102, 102)  # Gray
    
    # Separator line
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('━' * 40)
    run.font.color.rgb = RGBColor(0, 51, 102)
    
    # Author
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f'作者：{author}')
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(51, 51, 51)
    
    # Date
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f'日期：{date}')
    run.font.size = Pt(14)
    run.font.color.rgb = RGBColor(51, 51, 51)
    
    # Page break after cover
    doc.add_page_break()


def add_toc(doc):
    """Add a Table of Contents field (3-level, update in Word)."""
    # TOC title
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('目  录')
    run.font.size = Pt(18)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0, 51, 102)
    
    # Add TOC field
    p = doc.add_paragraph()
    run = p.add_run()
    fldChar1 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="begin"/>')
    run._r.append(fldChar1)
    
    run = p.add_run()
    instrText = parse_xml(f'<w:instrText {nsdecls("w")} xml:space="preserve"> TOC \\o "1-3" \\h \\z \\u </w:instrText>')
    run._r.append(instrText)
    
    run = p.add_run()
    fldChar2 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="separate"/>')
    run._r.append(fldChar2)
    
    run = p.add_run('（请在 Word 中右键此处，选择"更新域"以生成目录）')
    run.font.color.rgb = RGBColor(128, 128, 128)
    run.font.italic = True
    
    run = p.add_run()
    fldChar3 = parse_xml(f'<w:fldChar {nsdecls("w")} w:fldCharType="end"/>')
    run._r.append(fldChar3)
    
    # Page break after TOC
    doc.add_page_break()


def set_table_style(table):
    """Style a table with blue header and alternating rows."""
    # Set table alignment
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # Style header row
    for cell in table.rows[0].cells:
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="003366" w:val="clear"/>')
        cell._tc.get_or_add_tcPr().append(shading)
        for paragraph in cell.paragraphs:
            for run in paragraph.runs:
                run.font.color.rgb = RGBColor(255, 255, 255)
                run.font.bold = True
                run.font.size = Pt(10)
    
    # Style data rows with alternating colors
    for i, row in enumerate(table.rows[1:], 1):
        color = "F2F7FB" if i % 2 == 0 else "FFFFFF"
        for cell in row.cells:
            shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color}" w:val="clear"/>')
            cell._tc.get_or_add_tcPr().append(shading)
            for paragraph in cell.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(10)


def parse_markdown_table(lines, start_idx):
    """Parse a markdown table starting at start_idx. Returns (table_data, end_idx)."""
    table_data = []
    idx = start_idx
    
    while idx < len(lines):
        line = lines[idx].strip()
        if not line.startswith('|'):
            break
        
        # Skip separator line (|---|---|)
        if re.match(r'^\|[\s\-:]+\|$', line):
            idx += 1
            continue
        
        # Parse row
        cells = [cell.strip() for cell in line.split('|')[1:-1]]
        if cells:
            table_data.append(cells)
        idx += 1
    
    return table_data, idx


def process_markdown(doc, md_content):
    """Process markdown content and add to document."""
    lines = md_content.split('\n')
    i = 0
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        # Skip empty lines
        if not stripped:
            i += 1
            continue
        
        # H1 heading
        if stripped.startswith('# ') and not stripped.startswith('## '):
            # Page break before H1 (except first one)
            if len(doc.paragraphs) > 10:
                doc.add_page_break()
            
            heading_text = stripped[2:].strip()
            p = doc.add_heading(heading_text, level=1)
            for run in p.runs:
                run.font.color.rgb = RGBColor(0, 51, 102)
            i += 1
            continue
        
        # H2 heading
        if stripped.startswith('## '):
            heading_text = stripped[3:].strip()
            p = doc.add_heading(heading_text, level=2)
            for run in p.runs:
                run.font.color.rgb = RGBColor(0, 76, 153)
            i += 1
            continue
        
        # H3 heading
        if stripped.startswith('### '):
            heading_text = stripped[4:].strip()
            p = doc.add_heading(heading_text, level=3)
            for run in p.runs:
                run.font.color.rgb = RGBColor(51, 102, 153)
            i += 1
            continue
        
        # H4 heading
        if stripped.startswith('#### '):
            heading_text = stripped[5:].strip()
            p = doc.add_heading(heading_text, level=4)
            i += 1
            continue
        
        # Table
        if stripped.startswith('|'):
            table_data, end_idx = parse_markdown_table(lines, i)
            if table_data and len(table_data) > 0:
                # Create table
                num_cols = max(len(row) for row in table_data)
                table = doc.add_table(rows=len(table_data), cols=num_cols)
                table.style = 'Table Grid'
                
                # Fill table
                for row_idx, row_data in enumerate(table_data):
                    for col_idx, cell_text in enumerate(row_data):
                        if col_idx < num_cols:
                            table.rows[row_idx].cells[col_idx].text = cell_text
                
                # Style table
                try:
                    set_table_style(table)
                except Exception:
                    pass  # Skip styling if it fails
                
                doc.add_paragraph()  # Space after table
            i = end_idx
            continue
        
        # Code block
        if stripped.startswith('```'):
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('```'):
                code_lines.append(lines[i])
                i += 1
            i += 1  # Skip closing ```
            
            # Add code as formatted paragraph
            if code_lines:
                p = doc.add_paragraph()
                run = p.add_run('\n'.join(code_lines))
                run.font.name = 'Consolas'
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(51, 51, 51)
                # Add light gray background
                shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F5F5F5" w:val="clear"/>')
                p._p.get_or_add_pPr().append(shading)
            continue
        
        # Bullet points
        if stripped.startswith('- ') or stripped.startswith('* '):
            text = stripped[2:].strip()
            p = doc.add_paragraph(text, style='List Bullet')
            i += 1
            continue
        
        # Numbered list
        if re.match(r'^\d+\.\s', stripped):
            text = re.sub(r'^\d+\.\s', '', stripped)
            p = doc.add_paragraph(text, style='List Number')
            i += 1
            continue
        
        # Blockquote
        if stripped.startswith('> '):
            text = stripped[2:].strip()
            p = doc.add_paragraph()
            p.paragraph_format.left_indent = Cm(1)
            run = p.add_run(text)
            run.font.italic = True
            run.font.color.rgb = RGBColor(102, 102, 102)
            i += 1
            continue
        
        # Horizontal rule
        if stripped in ['---', '***', '___']:
            p = doc.add_paragraph()
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run('─' * 50)
            run.font.color.rgb = RGBColor(200, 200, 200)
            i += 1
            continue
        
        # Checkbox list
        if stripped.startswith('- [ ]') or stripped.startswith('- [x]'):
            text = stripped[5:].strip()
            checked = '[x]' in stripped[:5]
            prefix = '☑' if checked else '☐'
            p = doc.add_paragraph(f'{prefix} {text}')
            i += 1
            continue
        
        # Regular paragraph
        # Handle inline formatting
        text = stripped
        p = doc.add_paragraph()
        
        # Simple inline formatting handling
        # Bold: **text** or __text__
        # Italic: *text* or _text_
        # Code: `text`
        
        parts = re.split(r'(\*\*.*?\*\*|__.*?__|`.*?`|\*.*?\*|_.*?_)', text)
        for part in parts:
            if part.startswith('**') and part.endswith('**'):
                run = p.add_run(part[2:-2])
                run.font.bold = True
            elif part.startswith('__') and part.endswith('__'):
                run = p.add_run(part[2:-2])
                run.font.bold = True
            elif part.startswith('`') and part.endswith('`'):
                run = p.add_run(part[1:-1])
                run.font.name = 'Consolas'
                run.font.size = Pt(9)
                run.font.color.rgb = RGBColor(199, 37, 78)
            elif part.startswith('*') and part.endswith('*'):
                run = p.add_run(part[1:-1])
                run.font.italic = True
            elif part.startswith('_') and part.endswith('_'):
                run = p.add_run(part[1:-1])
                run.font.italic = True
            else:
                run = p.add_run(part)
        
        i += 1


def main():
    parser = argparse.ArgumentParser(description='Convert TRIZ Markdown report to Word')
    parser.add_argument('input', help='Input Markdown file')
    parser.add_argument('output', help='Output Word file')
    parser.add_argument('--author', default='TRIZ Innovation Toolkit', help='Author name')
    parser.add_argument('--title', default=None, help='Report title (auto-detected from H1 if not set)')
    parser.add_argument('--subtitle', default='TRIZ 系统化创新分析报告', help='Report subtitle')
    
    args = parser.parse_args()
    
    input_path = Path(args.input)
    if not input_path.exists():
        print(f'Error: Input file not found: {input_path}')
        sys.exit(1)
    
    # Read markdown content
    md_content = input_path.read_text(encoding='utf-8')
    
    # Auto-detect title from first H1 if not specified
    title = args.title
    if not title:
        match = re.search(r'^#\s+(.+)$', md_content, re.MULTILINE)
        if match:
            title = match.group(1).strip()
        else:
            title = input_path.stem
    
    # Create document
    doc = Document()
    
    # Set margins
    for section in doc.sections:
        section.top_margin = Cm(2.54)
        section.bottom_margin = Cm(2.54)
        section.left_margin = Cm(3.18)
        section.right_margin = Cm(3.18)
    
    # Set default font
    style = doc.styles['Normal']
    font = style.font
    font.name = 'Microsoft YaHei'  # 微软雅黑 for Chinese
    font.size = Pt(11)
    
    # Create cover page
    from datetime import datetime
    date_str = datetime.now().strftime('%Y年%m月%d日')
    create_cover_page(doc, title, args.subtitle, args.author, date_str)
    
    # Add TOC
    add_toc(doc)
    
    # Process markdown content
    process_markdown(doc, md_content)
    
    # Save document
    output_path = Path(args.output)
    doc.save(str(output_path))
    
    size = output_path.stat().st_size
    print(f'Done: {output_path} ({size / 1024:.1f} KB)')
    print(f'Note: Open in Word and right-click TOC → "Update Field" to generate directory')


if __name__ == '__main__':
    main()
