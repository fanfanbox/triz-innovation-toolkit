# EPO OPS 配置指南

## 概述

EPO OPS（Open Patent Services）是欧洲专利局提供的免费 API，覆盖 **90+ 国家**的专利数据。

## 注册流程

1. 访问 https://developers.epo.org/
2. 注册账号并验证邮箱
3. 创建应用获取 Consumer Key 和 Secret
4. 等待应用状态变为 "approved"

## 认证方式

EPO OPS 使用 OAuth2 认证，需要 Base64 编码的 Consumer Key:Secret：

```python
import base64

credentials = f"{consumer_key}:{consumer_secret}"
encoded = base64.b64encode(credentials.encode()).decode()

headers = {
    "Authorization": f"Basic {encoded}",
    "Content-Type": "application/x-www-form-urlencoded"
}

# 获取令牌
resp = requests.post(
    "https://ops.epo.org/3.2/auth/accesstoken",
    headers=headers,
    data={"grant_type": "client_credentials"}
)
```

## 常见问题

### 401 "Client credentials are invalid"

- 检查 Consumer Key 和 Secret 是否正确
- 确认应用状态为 "approved"
- 新创建的应用可能需要几分钟激活

### expires_in 类型错误

EPO OPS 返回的 `expires_in` 是字符串，需要转换：

```python
# ❌ 错误
self.token_expires = time.time() + data.get("expires_in", 3600) - 60

# ✅ 正确
self.token_expires = time.time() + int(data.get("expires_in", 3600)) - 60
```

## 环境变量配置

```bash
# Windows
set EPO_CONSUMER_KEY=your_consumer_key
set EPO_CONSUMER_SECRET=your_consumer_secret

# Linux/Mac
export EPO_CONSUMER_KEY=your_consumer_key
export EPO_CONSUMER_SECRET=your_consumer_secret
```

## API 端点

| 端点 | 说明 |
|------|------|
| `https://ops.epo.org/3.2/auth/accesstoken` | OAuth2 令牌获取 |
| `https://ops.epo.org/3.2/rest-services/published-data/search` | 专利检索 |

## 检索语法

使用 CQL（Common Query Language）：

```python
# 标题检索
cql_query = 'ta="phase change material"'

# 多关键词
cql_query = 'ta="phase change material" AND ta="thermal management"'

# 申请人检索
cql_query = 'pa="Toyota"'
```

## 限制

- 免费账户：无请求限制（非商业用途）
- 令牌有效期：1200 秒（20 分钟）
- 每次最多返回 100 条结果
