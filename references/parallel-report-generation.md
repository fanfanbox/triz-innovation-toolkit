# Parallel Report Generation Workflow

## Overview

For reports requiring 100+ pages, split generation into 3 parallel subagents and merge. Output in 3 formats: .md, .docx, .pdf.

## Workflow

### Step 1: Launch 3 Parallel Subagents

```
Subagent 1: Phase 1 — Problem Analysis (~40 pages)
  - 1.1 Topic Collection (3 rounds Q&A)
  - 1.2 Topic Organization (10 analysis items)
  - 1.3 Function Analysis
  - 1.4 Trimming
  - 1.5 Causal Chain Analysis
  - 1.6 Focus on Key Issues

Subagent 2: Phase 2 — Solution Generation (~40 pages)
  - 11-question routing diagnosis
  - Triz-AI patent mining
  - Contradiction matrix + 40 principles
  - Physical contradiction analysis (separation principles)
  - Su-Field analysis + 76 standard solutions
  - Function-oriented search (cross-industry)
  - Comprehensive solution matrix (4-dimension cross)
  - ARIZ-85C deep analysis
  - Extended patent panorama
  - Solution specification

Subagent 3: Phase 3 — Implementation (~25 pages)
  - Implementation roadmap (short/mid/long-term)
  - Prototype concept design
  - Conclusion
  - Appendix: Checklists + Quality self-assessment
```

### Step 2: Monitor Completion

```bash
ls -lh /path/to/TRIZ_报告_*_第*部分.md
```

Typical generation times:
- Part 1: 5-8 minutes
- Part 2: 8-20 minutes (longest due to patent analysis)
- Part 3: 5-8 minutes

### Step 3: Merge Reports

```bash
cat "报告_第一部分.md" "报告_第二部分.md" "报告_第三部分.md" > "报告_完整版.md"
```

### Step 4: Generate Word Document (USE THIS, NOT PANDOC)

```bash
# Single file
python scripts/triz_md_to_docx.py "报告_完整版.md" "报告_完整版.docx" --author "作者名"

# Batch conversion
for file in TRIZ_*_完整版.md; do
  python scripts/triz_md_to_docx.py "$file" "${file%.md}.docx" --author "作者名"
done
```

**Why NOT pandoc:**
- Pandoc cannot generate correct 3-level TOC with working links
- Pandoc cannot generate cover pages with author info
- Pandoc cannot set chapter breaks before H1 headings
- Pandoc table styling is limited

**Why use triz_md_to_docx.py:**
- Cover page with title, subtitle, author, date
- 3-level TOC with hyperlinks (update in Word after opening)
- Auto page break before H1 headings
- Professional table styling (blue header, alternating rows)
- Proper margins (2.54cm top/bottom, 3.18cm left/right)

### Step 5: Convert to PDF

```bash
pip install docx2pdf
python -c "from docx2pdf import convert; convert('报告_完整版.docx', '报告_完整版.pdf')"
```

## File Naming Convention

```
TRIZ_报告_<课题名称>_第一部分.md   # Phase 1
TRIZ_报告_<课题名称>_第二部分.md   # Phase 2
TRIZ_报告_<课题名称>_第三部分.md   # Phase 3
TRIZ_报告_<课题名称>_完整版.md     # Merged
TRIZ_报告_<课题名称>_完整版.docx   # Word (with cover+TOC+breaks)
TRIZ_报告_<课题名称>_完整版.pdf    # PDF
```

## Typical File Sizes

| Component | Size | Pages |
|-----------|------|-------|
| Part 1 (Problem Analysis) | 50-90 KB | ~30-40 |
| Part 2 (Solution Generation) | 80-110 KB | ~35-45 |
| Part 3 (Implementation) | 45-115 KB | ~25-35 |
| **Merged Complete** | **180-280 KB** | **90-120** |
| **Word** | 120-165 KB | — |
| **PDF** | 6.5-7.5 MB | — |

## Pitfalls

### ⚠️ Do NOT Use Pandoc for Word

Pandoc cannot generate:
- Correct 3-level TOC with working links
- Cover page with author info
- Chapter breaks before H1
- Professional table styling

Always use `scripts/triz_md_to_docx.py` (python-docx based).

### ⚠️ TOC Needs Manual Update

After opening the Word document, right-click the TOC area → "Update Field" → "Update entire table" to generate the 3-level directory with links.

### ⚠️ Subagent Timeout

Part 2 (Solution Generation) often takes 15-20+ minutes due to extensive patent analysis. Monitor with:
```bash
sleep 120 && ls -lh /path/to/TRIZ_报告_*_第*部分.md
```

### ⚠️ File Not Found During Merge

If a part file is missing, the subagent may still be running. Wait and retry.

### ⚠️ docx2pdf Requires Microsoft Word

On Windows, docx2pdf uses Microsoft Word to convert. If Word is not installed, the conversion will fail. Alternative: use LibreOffice (`soffice --headless --convert-to pdf`).
