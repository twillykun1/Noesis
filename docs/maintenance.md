# 安装与验证维护

## 安装包

只安装 `skills/noesis`，内容为：

- `SKILL.md`：核心指令，按用户语言回应。
- `references/complex-projects.md`：跨模块、跨服务或证据冲突时按需加载。
- `references/review.md`：可选独立复核。
- `references/preferences.md`：有长期偏好读写需求时加载，含具体宿主路径与边界。
- `examples/scenarios.md`：情境示例，不是已执行验证。
- `templates/decision-record.md`：可选项目简报，优先复用现有记录。

安装器目标以其实际返回为准，不把一个目录当作所有宿主的通用约定。遵循安装器关于新会话或重启的说明。需要固定版本时，通过官方安装器的 `--ref` 指定真实完整提交 SHA；`main` 会变化。

更新：安装到单独临时目录，比较与备份原安装，取得替换授权后再替换。卸载：仅在用户要求时删除实际安装的 `noesis` 目录，不删除整个 skills 目录。仓库不提供自动更新器或网络 shell 安装器。

## 私有偏好与宿主能力

个人解释偏好由宿主已有的私有记忆或已建立的用户级记录负责，不属于六文件安装包，也不写入共享项目记录。具体位置、写入权限与后续读取方式必须依据实际宿主确认；不把某个固定路径当成通用约定。没有可用能力时仅在当前会话调整，不新增数据库、监听器或自动画像。

只保存明确长期要求或确认过的共识，保留具体做法、范围、简短来源和日期。普通回应不单独构成证据，但对清楚的长期确认问题的简短回答可以确认。当前要求优先；临时例外不改长期项，长期修正则合并或替换旧项。写入成功、后续实际读取和行为有效是不同证据，分别报告，不承诺自动跨会话、跨设备或跨宿主同步。

### Codex 保存到哪里、下次怎么读

默认保存位置是 `~/.codex/AGENTS.md` 的 `## Noesis communication preferences` 小节，复用已有对应条目，不覆盖整份用户指令。若设置了 `CODEX_HOME`，改用该目录；macOS/Linux 的 `~` 是当前用户 home，原生 Windows 默认 `%USERPROFILE%\.codex\AGENTS.md`，WSL 使用 Linux home。

这只适用于支持用户级 AGENTS 的 Codex 运行环境。写前确认解析后的路径私有、可授权写入、没有落在共享/可发布仓库或技能目录。已有非空 `AGENTS.override.md` 会遮蔽同目录 `AGENTS.md`；有旧偏好被遮蔽或 override 可能只是临时文件时，先说明并确认维护位置，不擅自迁移或复制。用户请求只涉及本次开发时，不顺便改其真实全局配置。

原生 Codex 在新一轮运行启动时读取全局指令；当前会话不会因磁盘写入自动刷新。Noesis 开始相关任务或话题改变时，优先使用上下文中的相关偏好，否则从确认过的有效用户级文件读取。其他宿主采用其已支持的私有记忆入口，没有入口则只在当前对话调整。此机制不是跨设备同步，也不保证技能每次自动触发。

读取顺序、`CODEX_HOME` 与长度限制见 [Codex 官方 AGENTS 文档](https://learn.chatgpt.com/docs/agent-configuration/agents-md)。运行时的完整边界见 [私有偏好参考](../skills/noesis/references/preferences.md)。

## 维护命令

```sh
python3 scripts/check_package.py
python3 -m unittest discover -s tests -v
```

结构检查验证限定文件集、frontmatter、UTF-8、相对引用和文件类型。安装集成测试使用本机 Codex 官方 `install-skill-from-github.py`；可用 `NOESIS_OFFICIAL_INSTALLER` 指定脚本位置。只将源码获取步骤替换为临时本地候选目录，实际调用安装器的参数解析、路径校验、复制和已有目标拒绝逻辑。测试核对六文件及内容哈希、重复安装不覆盖、不安全路径和符号链接被拒绝。目标在临时目录，不修改全局技能。缺少安装器时测试明确跳过，报告不得写成全部安装验证通过。

这是本地源码注入测试，不是公开 GitHub 下载、宿主自动发现或原生加载测试。候选修改发布前也不能用远端旧版本的安装结果证明新版本已安装。发布后可用固定提交 SHA 在临时目标复测远端下载与内容哈希，单独记录结果。

`tests/test_codex_preferences.py` 使用临时 `CODEX_HOME` 和虚构标记，调用本机 `codex debug prompt-input`，检查用户文件进入启动输入、修改后新运行读取新值、override 遮蔽及空 override 回退。不会调用模型，不复制认证，不改真实用户配置。可用 `NOESIS_CODEX_CLI` 指定 Codex 可执行文件；缺少 CLI 或该调试命令时明确跳过。

## 行为验证边界

包结构和安装测试不验证 AI 是否正确追踪系统后果。内容回归应给独立评估者具体的小型代码、配置、需求和真实标明来源的测试记录，分别检查结论、信息依据与沟通负担；检查原始回答而不是只匹配标题或关键词。至少覆盖下游消费者、配置使旧证据过期、外部依赖不可访问、重复副作用、业务约束变化和普通文案改动。

只读材料评估不等于执行代码、集成环境验证或真人理解测试；不得将其当作已证明的收益。v0.1 历史评测不代表 v0.3 效果。当前没有 v0.4 的效果提升或跨宿主兼容性结论。新验证记录见 [v0.4 验证](verification-v0.4.0.md)，设计依据与迁移边界见 [沟通设计](communication-design.md)。

根目录 `SKILL.md` 是旧入口提示；`DESIGN.md`、根目录 examples/references/templates 和 evals 是保留的历史资料，不属于运行时包。
