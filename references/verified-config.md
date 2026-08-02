# 已验证的配置和环境状态

*最后验证：2026-07-22*

## 当前环境状态

| 组件 | 状态 | 版本/路径 |
|------|------|-----------|
| **TrizInv Skill** | ✅ 已安装 | `~/.hermes/skills/triz-innovation-toolkit/` |
| **triz-ai CLI** | ✅ 已安装 | v0.18.1 (Python 3.14) |
| **Ollama** | ✅ 运行中 | localhost:11434 |
| **nomic-embed-text** | ✅ 已安装 | 274 MB |
| **MiMo API** | ✅ 可用 | mimo-v2.5-pro |
| **Python** | ✅ 3.14.6 | `C:\Users\jianw\AppData\Local\Programs\Python\Python314\python.exe` |

## 已验证的 triz-ai 配置

**文件位置**：`~/.triz-ai/config.yaml`

```yaml
llm:
  default_model: mimo-v2.5-pro
  classify_model: mimo-v2.5
  deep_model: mimo-v2.5-pro
  reasoning_effort: medium
  api_base: https://api.xiaomimimo.com/v1
  api_key: <从 ~/.hermes/.env 读取 XIAOMI_API_KEY>

embeddings:
  model: nomic-embed-text
  dimensions: 768
  api_base: http://localhost:11434/v1
  api_key: ollama

database:
  path: ~/.triz-ai/patents.db
```

## MiMo API 可用模型（已验证）

| 模型 | ID | 用途 |
|------|-----|------|
| MiMo v2.5 | `mimo-v2.5` | 分类（快速） |
| MiMo v2.5 Pro | `mimo-v2.5-pro` | 主分析/深度分析 |
| MiMo v2.5 ASR | `mimo-v2.5-asr` | 语音识别 |
| MiMo v2.5 TTS | `mimo-v2.5-tts` | 语音合成 |

**⚠️ 不存在的模型**：`mimo-v2-pro`, `mimo-v2-flash`, `mimo-v2.5-flash`

## 已验证的命令

```bash
# 运行环境设置（必须）
export PYTHONPATH="" && export PATH="/c/Users/jianw/AppData/Local/Programs/Python/Python314:/c/Users/jianw/AppData/Local/Programs/Python/Python314/Scripts:$PATH"

# 矛盾矩阵统计
triz-ai matrix stats
# 结果：填充率 95.7%，2450 单元格，2345 已填充

# 领域专利发现
triz-ai discover --domain "新能源汽车永磁同步电机"
# 结果：136 件专利，5 个低频原理

# 问题分析
triz-ai analyze "问题描述"
# 结果：自动路由到 technical-contradiction，推荐原理 + 方案方向
```

## 已验证的 Git 仓库

| 仓库 | URL | 分支 |
|------|-----|------|
| triz-innovation-toolkit | https://github.com/fanfanbox/triz-innovation-toolkit | main |
| 最新版本 | v3.2.0 | 2026-07-22 |

## Ollama 已安装模型

| 模型 | 大小 | 用途 |
|------|------|------|
| nomic-embed-text:latest | 274 MB | 向量嵌入（triz-ai 必需） |
| qwen2.5vl:3b | 3.2 GB | 视觉语言模型 |
| deepseek-coder:1.3b | 776 MB | 代码生成 |

## 已验证的报告生成数据

| 课题 | 大小 | 页数 | 生成时间 |
|------|------|------|----------|
| 主驱电机小型化 | 243 KB | ~98页 | ~10 min |
| 电涡流传感器 | 251 KB | ~117页 | ~12 min |
| 电磁优化设计 | 240 KB | ~92页 | ~10 min |
| 槽内油冷方案 | 281 KB | ~114页 | ~15 min |
| 母线电容设计 | 217 KB | ~106页 | ~15 min |

## GitHub Releases

| 版本 | 日期 | 主要更新 |
|------|------|----------|
| v3.2.0 | 2026-07-22 | 报告质量自评（10维度评估） |
| v3.1.0 | 2026-07-22 | 报告详细度要求 |
| v3.0.0 | 2026-07-22 | 四维度TRIZ分析、ARIZ-85C、专利全景 |
| v2.1.0 | 2026-07-22 | 恢复路径选择网关、11题问题路由 |
| v2.0.0 | 2026-07-22 | 集成Triz-AI、三阶段流程 |
| v1.0.0 | 2026-07-21 | 初始版本 |
