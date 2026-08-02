## 10. triz_md_to_docx.py Script Was Missing (v3.4.0 → v3.4.1)

**Issue**: SKILL.md referenced `scripts/triz_md_to_docx.py` for Word generation, but only `scripts/convert_to_word.sh` (pandoc-based) existed. The skill explicitly says NOT to use pandoc, creating a contradiction.

**Resolution**: Created the full `triz_md_to_docx.py` script using python-docx with:
- Cover page (title + subtitle + author + date)
- 3-level TOC via Word field codes (update in Word after opening)
- Page breaks before H1 headings
- Table styling (blue header #003366, alternating row colors)
- Margins: 2.54cm top/bottom, 3.18cm left/right
- Inline formatting support (bold, italic, code, bullet lists, numbered lists, blockquotes)
- Auto-detect title from first H1 heading

**Lesson**: When a skill references a script, verify it exists at load time. If missing, create it before running the workflow.

## 11. Windows/MSYS Path Conversion Pitfall

**Issue**: Running `python "C:\Users\..."` or `python "/c/Users/..."` in MSYS/Git Bash causes path double-escaping (`C:\\c\\Users\\...`).

**Root cause**: MSYS auto-converts POSIX paths to Windows paths (`MSYS_NO_PATHCONV`), but when paths are already in Windows format inside quotes, the backslashes get escaped.

**Fix**: Always use forward-slash Windows paths: `python "C:/Users/jianw/..."`.

**Verified**: 2026-07-29, Windows 10 + Git Bash + Python 3.14.

## 12. docx2pdf Requires Microsoft Word on Windows

**Issue**: `docx2pdf` on Windows uses Microsoft Word COM automation. If Word is not installed, conversion fails silently or with COM error.

**Fallback**: Use LibreOffice: `soffice --headless --convert-to pdf report.docx`

**Verified**: 2026-07-29, Windows 10 + MS Word 2019.

## 13. Convergent → Radial Transfer Pattern

**Pattern**: When user selects Convergent path, the dialogue converges in 2-3 rounds (problem scenario → contradiction identification → boundary confirmation). After user confirms, immediately dispatch 3 parallel subagents for the Radial phase.

**Key**: The Convergent phase produces a structured "problem definition card" that becomes the context for all 3 subagents:
- 课题名称
- 问题定义
- 5大部件 + 温度范围
- 核心矛盾 (3 technical + 1 physical)
- IFR
- 痛点排序

**Verified**: 2026-07-29, PHEV多级相变热管理课题.

## 14. patent_search.py v2.0 Created with Multi-Source Search

**Issue**: Original triz-ai only searched CNIPA (Chinese patents). Need global patent coverage.

**Resolution**: Created `scripts/patent_search.py` v2.0 with:
- Multi-source search: Lens.org, EPO OPS, PatentsView, BigQuery, Google Custom Search
- Hybrid search: vector + keyword (requires sentence-transformers)
- TRIZ principle auto-mapping: 40 principles + 12 technology categories
- Compliance checking: 35 USC 112 (written description, enablement, best mode, definiteness)
- Multiple export formats: JSON, CSV, Markdown

**Key API Status (as of 2026-07-30)**:
| API | Status | Requirement |
|-----|--------|-------------|
| Lens.org | ⚠️ Paid | $99/month minimum |
| EPO OPS | ❌ 403 | OAuth2 authentication required |
| PatentsView | ❌ Migrated | API endpoints changed, returns HTML |
| BigQuery | ⚠️ Setup | Requires Google Cloud project + service account |
| Google Custom Search | ⚠️ Setup | Requires API enabled + Search Engine ID |

**Verified**: 2026-07-30, Windows 10 + Python 3.14.

## 15. ComplianceChecker Class-Level self Reference Bug

**Issue**: `ComplianceChecker` class used `self._check_written_description` in a class-level dictionary, causing `NameError: name 'self' is not defined`.

**Root cause**: Python class-level code cannot reference `self` — it's only available in instance methods.

**Fix**: Move the REQUIREMENTS dictionary to `__init__` method:
```python
# ❌ Wrong
class ComplianceChecker:
    REQUIREMENTS = {
        "check": self._check_written_description,  # NameError!
    }

# ✅ Correct
class ComplianceChecker:
    def __init__(self):
        self.REQUIREMENTS = {
            "check": self._check_written_description,  # Works
        }
```

**Verified**: 2026-07-30, Python 3.14.

## 16. Google Custom Search API Configuration Pattern

**Pattern**: When using Google Custom Search API for patent search:
1. API Key alone is NOT sufficient
2. Must enable "Custom Search API" in Google Cloud Console (same project as API Key)
3. Must create a Custom Search Engine at https://programmablesearchengine.google.com/
4. Search Engine ID (cx parameter) is required for all queries
5. Rate limit: 100 queries/day free, then $5/1000 queries

**Configuration**:
```bash
set GOOGLE_API_KEY=your_api_key
set GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id
```

**Troubleshooting**:
- "Requests to this API are blocked" → Enable Custom Search API in Cloud Console
- "API key not valid" → Check API Key belongs to correct project
- "cx parameter required" → Create Custom Search Engine and get ID

**Verified**: 2026-07-30.

## 17. Patent Search Fallback Strategy

**When APIs fail, use this fallback chain**:
1. **Google Custom Search API** (if configured) → Most reliable
2. **Subagent browser search** → Use `delegate_task` with browser tools
3. **Google Patents API** (unofficial) → Rate-limited (~3 queries)
4. **Manual browser search** → Last resort

**Key insight**: Google Patents unofficial API (`patents.google.com/api/search`) works for 2-3 queries before 503 rate limit. Use multiple subagents in parallel to maximize coverage before rate limiting.

**Verified**: 2026-07-30, PHEV多级相变热管理专利检索.
