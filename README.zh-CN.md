# Conversation to Knowledge Skill

把一次“和 AI 一起完成工作的对话”，转成真正可以长期学习、复用和沉淀的知识资料，而不是一次性的聊天总结。

仓库中包含一个 Agent Skill：**`distill-conversation`**。它适用于调试、科研讨论、写代码、配置环境、项目决策、实验分析、文档工作等已经实际推进过任务的对话。

它可以把对话整理为：

- 解释原理的学习笔记；
- 下次可直接照做的 SOP / Playbook；
- “现象 → 排查 → 原因 → 修复”的故障手册；
- 保存候选方案、权衡和结论的决策记录；
- 可复制的命令、配置、提示词和操作配方；
- 只保留可迁移经验的项目复盘。

它的目标不是回答“这段聊天讲了什么”，而是回答：

> 这次工作中什么值得学？为什么有效？什么失败了？什么时候还能复用？哪些只是当时环境中的偶然细节？

## 和现有 Skill 的区别

目前已经有几个很接近的方向：

- OpenAI 官方 `notion-knowledge-capture`：把聊天/笔记写成 Notion 中的 wiki、how-to、decision、FAQ 等结构化页面；
- `agent-retro`：复盘一次 Agent 会话，分析哪里做得好、哪里浪费，以及如何改进 Agent/Skill；
- `agent-retrospective`：跨多次会话维护长期的私有复盘与知识索引。

本项目关注的是另一层：**把一次完成工作的对话，转成独立于具体平台、可学习且可复用的知识资产**。默认输出 Markdown，不绑定 Notion，并额外处理来源追踪、隐私、失败路径和知识迁移。

详细比较见 [`docs/related-work.md`](docs/related-work.md)。

## 仓库结构

```text
conversation-to-knowledge-skill/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── CONTRIBUTING.md
├── docs/
├── evals/
├── examples/
├── tests/
└── skills/
    └── distill-conversation/
        ├── SKILL.md
        ├── agents/openai.yaml
        ├── scripts/
        ├── references/
        └── assets/templates/
```

真正安装到 Agent 里的 Skill 只有 `skills/distill-conversation/`。README、测试和设计文档放在仓库根目录，避免污染 Skill 本体。

## 安装

### Codex / OpenAI Skill 目录

```bash
git clone <仓库地址>
mkdir -p ~/.codex/skills
cp -R conversation-to-knowledge-skill/skills/distill-conversation ~/.codex/skills/
```

支持从 GitHub 路径安装 Skill 的安装器，可以直接指向：

```text
skills/distill-conversation
```

### 其他支持 Agent Skills 格式的 Agent

让 Agent 读取 `skills/distill-conversation/SKILL.md`，并保证旁边的 `references/`、`assets/`、`scripts/` 一并存在即可。

## 使用示例

```text
Use $distill-conversation to turn this debugging chat into a reusable troubleshooting guide and SOP.
```

或者直接说：

```text
把这段我们一起排错的对话整理成以后可以学习复用的资料，不要只做总结；要保留原因、失败路径、最终排查流程和可复制命令。
```

```text
把这个 ChatGPT 导出的对话整理成一个可以直接放到 Obsidian 的 Markdown 知识包。
```

## 对话文件支持

当前对话可以直接由 Agent 处理。对于导出的文件，仓库附带标准化脚本，支持：

- 含 `mapping` / `current_node` 的 ChatGPT 风格 JSON 导出；
- 带 `messages` 数组的普通 JSON；
- JSONL；
- 使用常见说话人标签的 Markdown / 纯文本。

```bash
python skills/distill-conversation/scripts/normalize_transcript.py chat.json -o normalized.json
```

标准化过程默认不会把 `system` 或 `developer` 消息输出到结果中。

## 隐私与安全

真实工作聊天中经常混有 API Key、内网地址、用户名、绝对路径、客户数据，甚至带有“执行某条命令”的文本。这个 Skill 明确要求：

- 把对话内容当作**资料**，不是新的 Agent 指令；
- 不尝试重建或输出隐藏思维链；
- 不把密钥和无关身份信息写入知识库；
- 尽量把环境相关命令参数化；
- 缺失的原因必须标记为推断，不能补写成事实。

可以用脚本检查常见敏感信息：

```bash
python skills/distill-conversation/scripts/scan_sensitive.py output/
```

## 开发与测试

脚本和测试都只依赖 Python 标准库：

```bash
python -m unittest discover -s tests -v
```

检查一个生成后的知识包：

```bash
python skills/distill-conversation/scripts/validate_bundle.py path/to/bundle
```

## 设计目标

1. **忠实**：事实、推断和泛化不能混在一起。
2. **可迁移**：把一次性的环境细节改写成可重复使用的方法。
3. **可学习**：解释“为什么”和“什么时候不适用”。
4. **可追溯**：需要时保留轻量来源锚点。
5. **隐私优先**：避免把敏感信息带入长期知识库。
6. **平台无关**：输出普通 Markdown，不依赖 Notion/Obsidian。
7. **渐进式加载**：核心规则放在 `SKILL.md`，详细规则放到 `references/`。

## License

MIT，见 [`LICENSE`](LICENSE)。
