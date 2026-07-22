# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-07-22

### 🚀 重大更新：集成 Triz-AI 专利分析

本版本将 Triz-AI CLI 完全集成到 Skill 中，实现 TRIZ 方法论 + AI 专利挖掘的一体化。

### Added
- **Triz-AI CLI 集成** — 专利挖掘成为全局必选项，5 个触发点自动执行 triz-ai 命令
- **一键安装脚本** — `install.sh`（Linux/Mac）和 `install.bat`（Windows）
- **配置模板** — `config.yaml.template`，支持 MiMo API / Ollama / OpenRouter 三种方案
- **自动调用规则** — 用户陈述领域、发现矛盾、询问现有技术时自动调用 triz-ai
- **降级方案** — Triz-AI 不可用时自动使用 cheatsheet.md / patterns.md 缓存数据
- **6 种分析方法** — technical-contradiction, physical-contradiction, su-field, function-analysis, trimming, trends
- **Pitfalls 文档** — 4 个关键陷阱（模型前缀、embedding api_base、Python 版本冲突、MiMo 可用模型）

### Changed
- **SKILL.md 完全重写** — 整合 Triz-AI 内容，统一入口，版本升级到 2.0.0
- **README.md 更新** — 新增安装说明、功能特性、Triz-AI 配置指南
- **references/triz-ai-setup.md** — 新增 MiMo API 配置、Pitfalls 详解

### Technical Details
- MiMo API 模型：`mimo-v2.5`, `mimo-v2.5-pro`, `mimo-v2.5-asr`, `mimo-v2.5-tts`
- Ollama embedding：`nomic-embed-text` (768 维)
- Python 要求：>= 3.12（triz-ai CLI）
- 运行前需清除 PYTHONPATH 避免 Hermes venv 冲突

## [1.0.0] - 2026-07-21

### Added
- 初始版本发布
- 24 章完整 TRIZ 知识体系
- 双路径问题解决（放射型/收敛型）
- 11 题问题路由诊断
- 快速参考表（cheatsheet.md）
- 模式目录（patterns.md）
- 术语表（glossary.md）
- TRIZ 使用教程

### Knowledge Sources
- TRIZ For Dummies (Haines-Gadd, 2016)
- TRIZ Handbook (Livotov & Petrov)
- TRIZ POWER TOOLS (Ball)
- TRIZ for Engineers (Gadd)
- 金钥匙 I & 金钥匙2 (孙永伟)
- 创新算法 (Altshuller 中译本)
- 推动创新的技术 (Bukhman 中译本)
