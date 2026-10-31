# Noesis · v0.2.0

**Understand the work. Own the decision.**

帮助有开发经验的人进入陌生技术子领域：AI 自主调查、提出有项目后果的建议、实施和验证；用户掌握目标、风险与验收。只解释会影响选择的最少背景，不把协作变成术语考试或审批流程。

## 一句话安装

> 请使用你内置的 skill-installer，从 https://github.com/twillykun1/Noesis/tree/main/skills/noesis 安装 Noesis；若已安装，先说明差异再更新。

优先使用 Codex 官方 `skill-installer`。只安装仓库 https://github.com/twillykun1/Noesis 中的 `skills/noesis` 子目录及其四个文件；仓库根目录不是安装包。已有安装不得直接覆盖：“先说明差异再更新”包含先比较、备份，并取得用户对替换的明确确认；未确认前保留原版本。

以宿主工具实际返回的安装路径为准，不把某个路径当作所有 agent 的通用约定。本次检查的本地官方脚本默认使用 `$CODEX_HOME/skills`，未设置时使用 `~/.codex/skills`，也支持 `--dest`。按本地安装器说明在下一轮会话使用；本次没有验证原生技能发现或加载。其他 agent 的手动读取方式可尝试，但移植性未测试。

需要固定版本时，让安装器使用发布后真实的完整提交 SHA 作为 `--ref`，路径仍是 `skills/noesis`；此处不虚构发布标签或尚未生成的提交号。`main` 会随更新变化。

## 使用与维护

安装后可说：“使用 Noesis 帮我改造登录会话；先检查现状，关键取舍说明项目影响，已授权的工作继续推进。”可随时说“不懂 / 不同意 / 过细 / 没必要”；AI 应调整说明，并在反馈改变前提时调整实际计划。

更新时先安装到单独的临时目标，比较新旧文件并备份现有目录；获得用户明确更新授权后再替换。卸载必须由用户请求，只删除工具报告的那个已安装 `noesis` 目录，不删除整个 skills 目录。无需自制网络安装器或 `curl | sh`。

## 包与验证

运行时包只有：

- `skills/noesis/SKILL.md`：英文核心指令，按用户语言回应。
- `skills/noesis/examples/scenarios.md`：中文情境与下一步行动。
- `skills/noesis/references/review.md`：可选且如实标明工具的独立复核。
- `skills/noesis/templates/decision-record.md`：可接入现有记录的当前项目简报。

维护者可运行 `python3 scripts/check_package.py` 和 `python3 -m unittest discover -s tests -p 'test_package.py' -v`。`test_official_install.py` 使用本机官方安装器，将源码获取步骤替换为临时本地候选包，验证解析、校验、复制、拒绝覆盖与不安全路径；缺少官方脚本时明确跳过。它不是 GitHub 下载或自动发现测试，不联网、不全局安装。

结构检查不证明模型行为或决策质量提升。v0.2 未新增模型模拟或真实用户试验。根目录 `SKILL.md` 仅为旧入口提示；原有 `DESIGN.md`、根目录 examples/references/templates 与 evals 是历史资料，不属于运行时包，也不代表 v0.2 当前指令。

Markdown skill 不能保证每轮触发、监控或硬阻断操作；权限与工程规范由宿主和仓库负责。本仓库尚未附开源许可证，公开可见不等于授予开源使用许可。
