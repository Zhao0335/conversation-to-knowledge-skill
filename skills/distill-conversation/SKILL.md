---
name: distill-conversation
description: Turn completed AI-assisted work conversations or transcript files into durable, reusable learning artifacts such as learning notes, SOPs/playbooks, diagnostic guides, decision records, reusable recipes, and retrospectives. Use when the user asks to convert a chat/session/transcript into study material, a knowledge base entry, reusable documentation, lessons learned, a runbook, or reference material rather than a simple chronological summary. Do not trigger for ordinary one-off summarization when the user only wants a brief recap.
---

# Distill Conversation

Transform a work conversation into knowledge that remains useful after the chat itself is forgotten.

## Core rules

- Use the visible conversation, user-provided files, tool results, and produced artifacts as evidence.
- Separate confirmed facts from inference. Label uncertain conclusions instead of repairing gaps with invented rationale.
- Prefer reusable explanations and decision rules over chronology.
- Preserve failed approaches when they teach a useful diagnostic branch, boundary condition, or anti-pattern; otherwise omit them.
- Generalize one-off environment values when the exact value is not part of the lesson.
- Do not force every artifact type into every conversation.

## Workflow

### 1. Resolve the source

Use the current conversation directly when it contains the full work session. For an external transcript file, use `scripts/normalize_transcript.py` when normalization helps. Read `references/source-guide.md` for source-selection guidance.

### 2. Build an evidence ledger

Before drafting, identify:

- original goal or problem;
- constraints and assumptions;
- actions/tests performed;
- observable results;
- user corrections;
- decisions and alternatives;
- failed or abandoned approaches;
- final outcome and produced artifacts.

For each important item, distinguish **observed**, **stated**, and **derived** information. Keep lightweight source anchors when traceability would help.

### 3. Filter for durable knowledge

Classify candidate material as:

- **durable** — likely to help in a future similar task;
- **situational** — useful mainly for reconstructing this session;
- **environment-specific** — generalize when possible;
- **uncertain** — retain only with an explicit uncertainty label.

Prefer the durable layer in the final material. Keep situational context only when needed to understand why a lesson applies.

### 4. Select output artifacts

Read `references/output-taxonomy.md` and choose the smallest set that captures the durable value.

Typical choices:

- concept/explanation → learning note;
- repeatable successful sequence → playbook/SOP;
- symptom/test/cause/fix → diagnostic guide;
- alternatives/trade-offs/rationale → decision record;
- commands/config/prompt pattern → recipe/reference card;
- process-level lesson → retrospective.

Use a **compact single Markdown file** for short, single-topic conversations. Use a **modular bundle with `index.md`** when the source has multiple distinct reusable lessons.

Templates in `assets/templates/` are starting shapes, not mandatory schemas.

### 5. Teach, do not merely compress

For each durable lesson, add the minimum explanation needed to reuse it:

- what the pattern is;
- why it worked or failed;
- how to recognize when it applies;
- what evidence distinguishes nearby failure modes;
- what prerequisites or constraints matter;
- when the lesson should not be applied.

Rewrite environment-specific commands into parameterized forms when possible while preserving exact syntax that is itself instructional.

### 6. Preserve provenance without reproducing the chat

Do not dump the transcript into the output. When provenance matters, use compact anchors such as `[S12]` or a small source-notes section mapping a claim to message numbers, timestamps, file names, or tool outputs.

### 7. Run quality checks

Run `scripts/scan_sensitive.py` on generated files when a filesystem is available, then revise any output that needs generalization. Read `references/quality-rubric.md` and revise weak artifacts. When a filesystem is available, run `scripts/validate_bundle.py` for basic bundle integrity.

### 8. Deliver the knowledge artifact

Return or save the finished Markdown artifact(s), not only a prose description of what could be created.

If the user specified a knowledge-base destination or folder, preserve its existing conventions. Otherwise use neutral Markdown with descriptive file names.
