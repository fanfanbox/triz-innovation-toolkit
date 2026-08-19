# Triz-AI CLI 安装与配置

## 安装

triz-ai 需要 **Python >=3.12**。当前系统默认 Python 3.11.15，需要使用 Python 3.14：

```bash
# 使用系统已安装的 Python 3.14
"C:\Users\jianw\AppData\Local\Programs\Python\Python314\python.exe" -m pip install triz-ai --index-url https://pypi.tuna.tsinghua.edu.cn/simple

# 验证安装
triz-ai --help
```

## LLM 后端配置

创建配置文件 `~/.triz-ai/config.yaml`：

### 方案 A: MiMo API + Ollama 本地 Embedding（当前方案）

```yaml
llm:
  default_model: mimo-v2.5-pro       # 主分析
  classify_model: mimo-v2.5           # 分类（快速）
  deep_model: mimo-v2.5-pro           # ARIZ 深度分析
  reasoning_effort: medium
  api_base: https://api.xiaomimimo.com/v1
  api_key: ${XIAOMI_API_KEY}          # 从 ~/.hermes/.env 读取

embeddings:
  model: nomic-embed-text
  dimensions: 768
  api_base: http://localhost:11434/v1  # Ollama 本地端点
  api_key: ollama                      # Ollama 不验证 key
```

MiMo API 可用模型：`mimo-v2.5`, `mimo-v2.5-pro`, `mimo-v2.5-asr`, `mimo-v2.5-tts`

### 方案 B: Ollama 全本地（免费，离线，需安装大模型）

```yaml
llm:
  default_model: ollama/qwen2.5:7b
  classify_model: ollama/qwen2.5:7b
embeddings:
  model: nomic-embed-text
  dimensions: 768
```

### 方案 C: OpenRouter（需 API Key，模型多）

```yaml
llm:
  default_model: openrouter/deepseek/deepseek-chat
  classify_model: openrouter/nvidia/nemotron-3-nano-30b-a3b:free
embeddings:
  model: openrouter/nvidia/llama-nemotron-embed-vl-1b-v2:free
  dimensions: 768
```

## 已安装的 Ollama 模型

- `nomic-embed-text:latest` — 274 MB（向量嵌入）
- `qwen2.5vl:3b` — 3.2 GB（视觉语言模型）
- `deepseek-coder:1.3b` — 776 MB（代码模型）

## 已验证的运行命令

每次运行 triz-ai 前，必须在同一行中设置环境：

```bash
export PYTHONPATH="" && export PATH="/c/Users/jianw/AppData/Local/Programs/Python/Python314:/c/Users/jianw/AppData/Local/Programs/Python/Python314/Scripts:$PATH" && cd ~/.triz-ai && triz-ai <command>
```

`cd ~/.triz-ai` 确保 triz-ai 能找到 `.env` 文件中的 API Key。

## 命令速查

```bash
# 分析问题（自动路由）
triz-ai analyze "如何提高SiC MOSFET开关速度而不增加EMI"

# 深度分析（ARIZ-85C 3轮）
triz-ai analyze "问题" --deep

# 指定方法
triz-ai analyze "问题" --method technical-contradiction

# 发现领域低频原理
triz-ai discover --domain "电机设计"

# 矛盾矩阵统计
triz-ai matrix stats

# 导入专利
triz-ai ingest data/patents/

# 从专利发现新原理
triz-ai evolve --review
```

## 6 种分析方法

| 方法 | 场景 | 示例 |
|------|------|------|
| technical-contradiction | 改善X但恶化Y | 提升功率密度但温度升高 |
| physical-contradiction | 既要A又要B | 焊点既要刚性又要柔性 |
| su-field | 检测/测量问题 | 不加传感器检测分层 |
| function-analysis | 组件造成损害 | 粘接层在热循环中损伤芯片 |
| trimming | 简化/降本 | 降低驱动电路BOM成本 |
| trends | 技术走向预测 | SiC封装下一代技术？ |

## Pitfalls

### ⚠️ 模型名称不能带 `openai/` 前缀（关键）

triz-ai 未安装 litellm 时使用原生 OpenAI SDK，会把模型名**原样**发送到 API 端点。

```yaml
# ❌ 错误 — MiMo API 返回 "Unsupported model openai/mimo-v2.5-pro"
default_model: openai/mimo-v2.5-pro

# ✅ 正确 — 直接用模型 ID
default_model: mimo-v2.5-pro
```

只有安装了 `pip install triz-ai[litellm]` 后才能使用 `provider/model` 前缀格式。

### ⚠️ Embedding 必须单独配置 api_base

如果不在 `embeddings:` 下指定 `api_base`，triz-ai 会用 LLM 的 api_base（MiMo）去请求 embedding 模型，导致失败。Ollama 的 OpenAI 兼容端点是 `http://localhost:11434/v1`。

### ⚠️ Python 版本与 Hermes venv 冲突

triz-ai 安装在 Python 3.14 中，但 bash 默认 PATH 包含 Hermes venv，导致 pydantic 版本冲突：
```
ModuleNotFoundError: No module named 'pydantic_core._pydantic_core'
```

**运行前必须清除 PYTHONPATH：**
```bash
export PYTHONPATH="" && export PATH="/c/Users/jianw/AppData/Local/Programs/Python/Python314:/c/Users/jianw/AppData/Local/Programs/Python/Python314/Scripts:$PATH"
```

### ⚠️ 环境变量插值失败时创建 .env 文件

配置文件中 `${XIAOMI_API_KEY}` 如果环境变量未设置会报 `ConfigError`。**最可靠的方案**是在 `~/.triz-ai/.env` 中同时设置两个变量：

```bash
# ~/.triz-ai/.env
OPENAI_API_KEY=sk-cdf...your-key
XIAOMI_API_KEY=sk-cdf...your-key
```

triz-ai 的 OpenAI SDK 路径会读取 `OPENAI_API_KEY`，而配置文件插值使用 `XIAOMI_API_KEY`。两者都需要。

**⚠️ 必须 `cd ~/.triz-ai` 后再运行 triz-ai**，否则 `.env` 文件找不到。推荐将 `cd ~/.triz-ai` 加入运行命令中。

### ⚠️ MiMo API 可用模型

MiMo API 只支持以下模型 ID：
- `mimo-v2.5`
- `mimo-v2.5-pro`
- `mimo-v2.5-asr`
- `mimo-v2.5-tts`

不存在 `mimo-v2-pro` 或 `mimo-v2-flash`。使用不存在的模型会返回 "Unsupported model" 错误。

验证可用模型：
```bash
curl -s https://api.xiaomimimo.com/v1/models -H "Authorization: Bearer $XIAOMI_API_KEY"
```

### 其他注意

- triz-ai 所有版本要求 Python >=3.12，无法在 3.11 上安装
- Ollama embeddings 模型（nomic-embed-text）需要提前下载：`ollama pull nomic-embed-text`
- `--deep` 模式比普通分析慢很多，适合复杂问题
- 在 Windows Git Bash 中运行 triz-ai 时，`PYTHONPATH` 清除和 `PATH` 设置必须在同一行 export 中完成，否则子进程可能继承错误的环境
