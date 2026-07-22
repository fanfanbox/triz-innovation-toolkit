# TRIZ Innovation Toolkit 🚀

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.0.0-orange.svg)]()
[![Chapters](https://img.shields.io/badge/Chapters-24-blue)](./chapters/)
[![TRIZ Tools](https://img.shields.io/badge/TRIZ%20Tools-22-orange)]()
[![Platform](https://img.shields.io/badge/Platform-Hermes%20Agent-green)]()

> **面向 Hermes Agent 的 TRIZ 系统化创新 + AI 专利分析一体化工具包**
>
> 24 章完整知识体系 + Triz-AI 专利挖掘 CLI + 智能双路径问题解决

---

## 📋 目录

- [什么是 TRIZ？](#什么是-triz)
- [功能特性](#功能特性)
- [快速安装](#快速安装)
- [使用方法](#使用方法)
- [Triz-AI CLI 配置](#triz-ai-cli-配置)
- [24 章知识体系](#24-章知识体系)
- [问题路由诊断](#问题路由诊断)
- [变更日志](#变更日志)

---

## 什么是 TRIZ？

**TRIZ**（发明问题解决理论）是由 Genrich Altshuller 于 1946 年创立的系统化创新方法论，基于 200 万+ 专利分析提炼出的创新规律。

**本工具包将 TRIZ 方法论与 AI 专利挖掘结合，提供一站式创新问题解决方案。**

---

## 功能特性

### 🔬 TrizInv 知识层（Skill）

| 功能 | 说明 |
|------|------|
| 24 章完整知识体系 | 从基础到高级的 TRIZ 工具全覆盖 |
| 40 发明原理 | 解决技术矛盾的标准方案库 |
| 矛盾矩阵 (39×39) | 快速查找推荐原理 |
| 8 技术进化趋势 | 预测产品下一代形态 |
| 76 标准解 | 物场分析的标准解法 |
| ARIZ 5 步算法 | 超级难题的系统化求解 |
| AFI 预期失效识别 | 设计阶段预测潜在失效 |
| 双路径问题解决 | 放射型（全自动）/ 收敛型（对话教练） |

### 🤖 Triz-AI 数据层（CLI）

| 功能 | 说明 |
|------|------|
| `analyze` | 自动分类问题 → 路由到最佳 TRIZ 方法 |
| `analyze --deep` | ARIZ-85C 深度 3 轮分析 |
| `discover` | 发现某领域低频 TRIZ 原理（机会空白） |
| `matrix stats` | 矛盾矩阵统计 |
| `ingest` | 导入专利数据 |
| `evolve` | 从专利发现候选新原理 |

---

## 快速安装

### 方式 1: 一键脚本（推荐）

**Linux / macOS / WSL:**
```bash
curl -fsSL https://raw.githubusercontent.com/fanfanbox/triz-innovation-toolkit/main/install.sh | bash
```

**Windows (PowerShell / CMD):**
```cmd
git clone https://github.com/fanfanbox/triz-innovation-toolkit.git "%USERPROFILE%\.hermes\skills\triz-innovation-toolkit"
```

**Windows (Git Bash):**
```bash
bash install.bat
```

### 方式 2: 手动安装

```bash
# 1. 克隆到 Hermes skills 目录
cd ~/.hermes/skills
git clone https://github.com/fanfanbox/triz-innovation-toolkit.git

# 2. 安装 triz-ai（需要 Python >= 3.12）
pip install triz-ai

# 3. 配置 LLM 后端
cp config.yaml.template ~/.triz-ai/config.yaml
# 编辑 ~/.triz-ai/config.yaml 填入 API Key
```

### 方式 3: Hermes CLI

```bash
hermes skills tap add fanfanbox/triz-innovation-toolkit
hermes skills install triz-innovation-toolkit
```

---

## 使用方法

### 加载 Skill

```
/skill triz-innovation-toolkit
```

### 描述问题

```
我想提升 SiC MOSFET 的开关速度，但 EMI 会增大，如何解决？
```

AI 会自动：
1. 识别技术矛盾（Speed vs EMI）
2. 调用 `triz-ai discover` 进行专利挖掘
3. 推荐 TRIZ 原理（如 Mechanical Vibration、Dynamics）
4. 生成具体解决方案方向

### CLI 命令

```bash
# 分析问题
triz-ai analyze "SiC MOSFET 开关速度提升但 EMI 增大"

# 深度分析
triz-ai analyze "问题" --deep

# 发现领域机会
triz-ai discover --domain "电机设计"

# 矛盾矩阵统计
triz-ai matrix stats
```

---

## Triz-AI CLI 配置

### 环境要求

| 组件 | 要求 |
|------|------|
| Python | >= 3.12 |
| Ollama | 已安装（用于本地 embedding） |
| MiMo API | API Key（或其他 LLM 提供商） |

### 配置文件

创建 `~/.triz-ai/config.yaml`：

```yaml
# MiMo API + Ollama 本地 Embedding
llm:
  default_model: mimo-v2.5-pro
  classify_model: mimo-v2.5
  deep_model: mimo-v2.5-pro
  api_base: https://api.xiaomimimo.com/v1
  api_key: YOUR_API_KEY

embeddings:
  model: nomic-embed-text
  dimensions: 768
  api_base: http://localhost:11434/v1
  api_key: ollama
```

### Ollama 模型安装

```bash
# 安装 embedding 模型（必需）
ollama pull nomic-embed-text

# 安装大模型（可选，用于本地分析）
ollama pull qwen2.5:7b
```

### ⚠️ 关键 Pitfalls

1. **模型名称不能带 `openai/` 前缀** — MiMo API 返回 "Unsupported model"
2. **Embedding 必须单独配置 `api_base`** — 否则会用 LLM 的 api_base 请求 embedding
3. **Python 版本冲突** — 运行前清除 `PYTHONPATH` 避免 Hermes venv 冲突

详见 [references/triz-ai-setup.md](references/triz-ai-setup.md)

---

## 24 章知识体系

| 部分 | 章节 | 核心工具 |
|------|------|----------|
| **I 基础** | Ch01-02 | TRIZ 概述、五大思维支柱 |
| **II 核心矛盾工具** | Ch03-05 | 40 原理、矛盾矩阵、8 趋势、理想化方程 |
| **III 知识与思维** | Ch06-08 | 效应数据库、心理惯性突破、九屏幕法 |
| **IV 高级求解** | Ch09-13 | IFR、功能分析、物场分析、76 标准解 |
| **V 系统优化** | Ch14 | 裁剪 |
| **VI 算法方法** | Ch17-18 | ARIZ、AFI |
| **VII 商业创新** | Ch19-21 | 商业 TRIZ、10 步流程、客户收益分析 |
| **VIII 落地实施** | Ch22-24 | 实施方法论、CAI、企业培训 |

---

## 问题路由诊断

按顺序回答，第一个"Yes"指向起始工具：

1. 问题是否明确？ → 功能分析 / IFR
2. 什么类型的矛盾？ → 矛盾矩阵 / 分离原理
3. 需要预测未来？ → 8 趋势
4. 需要降本简化？ → 裁剪
5. 创意枯竭？ → SLP / DTC / 九屏幕
6. 物质-场问题？ → 76 标准解
7. 找实现功能的方法？ → 效应数据库
8. 超级难题？ → ARIZ
9. 预测预防失效？ → AFI
10. 商业/管理问题？ → 商业 TRIZ
11. 准备实施？ → 实施方法论

---

## 变更日志

### v2.0.0 (2026-07-22)

**重大更新：集成 Triz-AI 专利分析**

#### 新增
- ✅ Triz-AI CLI 集成 — 专利挖掘成为全局必选项
- ✅ 一键安装脚本 (`install.sh` / `install.bat`)
- ✅ 配置模板 (`config.yaml.template`)
- ✅ 自动调用规则 — 5 个触发点自动执行 triz-ai 命令
- ✅ 降级方案 — Triz-AI 不可用时使用缓存数据
- ✅ MiMo API + Ollama 本地 embedding 支持
- ✅ 6 种分析方法详解
- ✅ Pitfalls 文档 — 4 个关键陷阱

#### 更新
- 📝 SKILL.md 完全重写，整合 Triz-AI 内容
- 📝 README.md 更新安装说明和功能特性
- 📝 CHANGELOG.md 更新

#### 文件结构
```
triz-innovation-toolkit/
├── SKILL.md                    # 主入口（路径选择 + 工具路由 + Triz-AI 集成）
├── install.sh                  # Linux/Mac 安装脚本
├── install.bat                 # Windows 安装脚本
├── config.yaml.template        # Triz-AI 配置模板
├── chapters/                   # 24 章详细内容
│   ├── ch01-zero-to-triz.md
│   ├── ...
│   └── ch24-corporate-training.md
├── cheatsheet.md               # 快速参考表
├── patterns.md                 # 模式目录
├── glossary.md                 # 术语表
├── references/                 # 参考文档
│   ├── routing-and-tools.md
│   └── triz-ai-setup.md
├── README.md                   # 本文档
├── CHANGELOG.md                # 变更日志
└── LICENSE                     # MIT 许可证
```

### v1.0.0 (2026-07-21)

- 初始版本
- 24 章 TRIZ 知识体系
- 双路径问题解决（放射型/收敛型）
- 11 题问题路由诊断

---

## 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

## 致谢

知识来源：
- *TRIZ For Dummies* (Haines-Gadd, 2016)
- *TRIZ Handbook* (Livotov & Petrov)
- *TRIZ POWER TOOLS* (Ball)
- *TRIZ for Engineers* (Gadd)
- *金钥匙 I & 金钥匙2* (孙永伟)
- *创新算法* (Altshuller 中译本)
- *推动创新的技术* (Bukhman 中译本)
