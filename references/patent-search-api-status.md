# Patent Search API Status Report

> Last updated: 2026-07-30
> Environment: Windows 10, Python 3.14.6

## API Status Summary

| API | Status | Auth | Cost | Recommendation |
|-----|--------|------|------|----------------|
| **Lens.org** | ❌ 需付费 | Bearer Token | $99+/月 | 忽略（用户明确要求） |
| **EPO OPS** | ✅ 已配置 | OAuth2 | 免费（非商业） | 已配置 consumer_key/secret |
| **PatentsView** | ❌ API变更 | 无需 | 免费 | 需要更新API调用格式 |
| **BigQuery** | ⚠️ 需配置 | Google Cloud | 免费1TB/月 | 已安装，需服务账号 |
| **Google Patents** | ⚠️ 限流 | 无需 | 免费 | ~3次查询后503 |
| **Google Custom Search** | ⚠️ 需启用 | API Key | 免费100次/天 | 已配置Key，需启用API |

## Working Configuration

### Google Custom Search API

**Required Setup**:
1. Enable Custom Search API in Google Cloud Console
2. Create Custom Search Engine at https://programmablesearchengine.google.com/
3. Configure to search `patents.google.com/*`
4. Get Search Engine ID (cx parameter)

**Environment Variables**:
```bash
set GOOGLE_API_KEY=your_google_api_key
set GOOGLE_SEARCH_ENGINE_ID=your_cx_id
```

**Limits**: 100 queries/day free, $5/1000 queries after

### BigQuery

**Status**: google-cloud-bigquery v3.42.2 installed

**Required Setup**:
1. Create Google Cloud project
2. Enable BigQuery API
3. Create service account with "BigQuery User" role
4. Download JSON key file
5. Set `GOOGLE_APPLICATION_CREDENTIALS` environment variable

**Public Dataset**: `patents-public-data.patents.publications` (76M+ US patents)

**Environment Variables**:
```bash
set GOOGLE_APPLICATION_CREDENTIALS=C:\path\to\key.json
set GOOGLE_CLOUD_PROJECT=your-project-id
```

## Degradation Strategy

```
Priority 1: EPO OPS (✅ configured - OAuth2)
    ↓
Priority 2: Google Custom Search (needs API enabled + Search Engine)
    ↓
Priority 3: BigQuery (needs Google Cloud project)
    ↓
Priority 4: Subagent browser search (manual, slow but reliable)
    ↓
Priority 5: Google Patents API (rate-limited after ~3 queries)
    ↓
Priority 6: triz-ai local data + AI knowledge
```

## Lessons Learned

1. **Google Patents API is unreliable** - Rate-limits after 3 queries (503 error for 24+ hours)
2. **EPO OPS requires OAuth2** - Simple API key is not enough
3. **PatentsView API may have changed** - Returns empty responses
4. **Subagent parallel search** - Best workaround for rate limiting: 2-3 subagents each make 1-2 queries before being blocked
5. **Google Custom Search** - Requires both API key AND Custom Search Engine configuration

## Recommended Actions

| Priority | Action | Effect |
|----------|--------|--------|
| **High** | Enable Custom Search API in Google Cloud Console | Unlock Google Custom Search |
| **High** | Create Custom Search Engine for patents.google.com | Enable patent-specific search |
| **Medium** | Register for EPO OPS (free) | Access to European patents |
| **Medium** | Set up BigQuery service account | Access to 76M+ US patents |
| **Low** | Register Lens.org (paid) | Global patent coverage |
