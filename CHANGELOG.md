# Changelog

All notable changes to the TRIZ Innovation Toolkit.

---

## [v1.2.0] — 2026-07-17

### Added
- **问题解决路径选择 (Problem Solving Path Selection)**: 使用前自动推荐放射型或收敛型路径
  - **放射型 (Radial)** — TRIZ 分析师人格，一次输入全自动分析，静默输出报告，适用于问题边界清晰的场景
  - **收敛型 (Convergent)** — TRIZ 教练人格，苏格拉底式 4 阶段对话，产出问题定义书 + 执行路线图，适用于问题模糊、需要对齐认知的场景
- 路径推荐网关 (Gateway)：自动分析用户问题，推荐最优路径并附简短理由
- `TRIZ使用教程.md` Section 2: 完整的路径选择使用指南
- Triz-AI 专利挖掘设为全局必选项（两条路径均必经此节点）

### Changed
- `TRIZ使用教程.md` 全文章节重编号（Section 2 重新插入，原有 2-9 → 3-10，所有 H3 子节同步更新）
- `TRIZ使用教程.md` Section 8.1: Triz-AI 触发条件从可选变为必选，新增路径差异化执行说明
- `SKILL.md`: 新增路径推荐网关、双人格 prompt、Triz-AI 必选化

---

## [v1.1.0] — 2026-07-07

### Added
- `TRIZ使用教程.md`: 综合 TRIZ 工具使用教程（中文），覆盖问题路由、工具选择、6步解决流程、10步商业创新流程
- Section 9: TRIZ 工具速查参考（含输出格式规范）
- `.gitattributes`: 强制 LF 行尾，确保跨平台兼容

### Fixed
- LaTeX 公式渲染问题：`\text{...}` 替换为纯文本公式

### Changed
- `SKILL.md`: 新增报告生成工作流
- `.gitignore`: 新增 `report/` 目录排除
- 移除 `tutorial_claude_code_skills.md`（非 TRIZ 相关内容）

---

## [v1.0.0] — 2026-07-06

### Initial Release

- `SKILL.md` — 技能入口：YAML 元数据、问题路由、工具选择器、章节索引
- `chapters/ch01-*.md` ~ `ch24-*.md` — 24 章深度章节摘要
- `cheatsheet.md` — 速查表：39 参数、矛盾矩阵、路由流程图、检查清单
- `patterns.md` — 完整模式目录：40 发明原理、8 大进化趋势、76 标准解、ARIZ、AFI
- `glossary.md` — A-Z 术语定义
- `README.md` — 双语 (CN+EN) 项目说明
- `LICENSE` — CC BY-NC-SA 4.0
- `.gitignore` — 排除受版权保护的源书、临时文件、IDE/OS 文件

**Sources**: 8 本权威 TRIZ 著作（4 EN, 4 ZH）
