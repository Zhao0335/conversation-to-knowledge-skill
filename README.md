# Conversation to Knowledge Skill

Turn completed AI-assisted work conversations into durable, reusable learning material instead of disposable chat summaries.

This repository ships an Agent Skill named **`distill-conversation`** for conversations where a user and an AI actually did work together: debugging, research planning, coding, analysis, writing, configuration, project decisions, experiments, and other multi-step tasks.

The skill can produce:

- learning notes that explain the underlying concept;
- playbooks and SOPs that can be reused next time;
- symptom → test → cause → fix diagnostic guides;
- decision records that preserve alternatives and trade-offs;
- reusable command/config/prompt recipes;
- concise retrospectives focused on transferable lessons.

It deliberately does more than summarization. The output should answer not only “what happened?” but also “what can someone learn from this, when does it apply again, what failed, and why?”

[中文 README](README.zh-CN.md)

## Repository layout

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

The installable skill lives under `skills/distill-conversation/`. Repository documentation and examples stay outside the skill directory so the runtime package remains compact.

## Install

```bash
git clone https://github.com/Zhao0335/conversation-to-knowledge-skill.git
mkdir -p ~/.codex/skills
cp -R conversation-to-knowledge-skill/skills/distill-conversation ~/.codex/skills/
```

For compatible skill installers, point directly at:

```text
skills/distill-conversation
```

## Example prompts

```text
Use $distill-conversation to turn this debugging chat into a reusable diagnostic guide and SOP.
```

```text
Distill this project conversation into learning notes, decisions, failed approaches, and reusable commands. Do not just summarize it.
```

```text
Convert this completed ChatGPT work conversation into a small Markdown knowledge bundle that I can put into Obsidian.
```

## How it works

The workflow separates four layers:

1. evidence and observable outcomes from the source conversation;
2. reusable knowledge versus one-off session details;
3. the right artifact shape for each durable lesson;
4. a final quality pass focused on fidelity, transfer, actionability, and portability.

See `docs/design.md` for the design rationale and `examples/` for a worked debugging example.

## Development

The helper scripts use only the Python standard library.

```bash
python -m compileall -q skills/distill-conversation/scripts
python skills/distill-conversation/scripts/validate_bundle.py examples/expected-debugging-bundle
```

## License

MIT. See [`LICENSE`](LICENSE).
