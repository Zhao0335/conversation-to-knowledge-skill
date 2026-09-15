# Output taxonomy

Use this reference to decide what to create. Choose by evidence shape, not by habit.

## Compact knowledge note

Use when the conversation is short, single-topic, and contains one or two reusable lessons.

Include only the sections needed to explain the lesson, how to apply it, and any important boundary condition.

## Learning note

Use when the durable value is conceptual understanding.

Good content:

- concept or mechanism;
- intuitive explanation;
- evidence from the session that made the concept relevant;
- application pattern;
- common misconception or boundary condition;
- small example if it improves transfer.

Avoid turning a learning note into a chronology of who said what.

## Playbook / SOP

Use when a sequence of actions can be repeated in a future task.

Good content:

- trigger / entry condition;
- prerequisites;
- ordered diagnostic or execution steps;
- branch conditions;
- verification of success;
- rollback or stop conditions when relevant;
- anti-patterns exposed by the original session.

A playbook should let a future reader act without re-reading the source chat.

## Troubleshooting guide

Use when the session contained an incident, failure, or confusing symptom and the evidence narrowed possible causes.

Prefer the shape:

```text
symptom
→ discriminating check
→ observed result
→ likely cause branch
→ fix
→ verification
```

Retain failed hypotheses only when they help show how to distinguish causes.

## Decision record

Use when multiple credible options were compared or a non-obvious choice was made.

Capture:

- decision context;
- alternatives considered;
- decision criteria;
- chosen option;
- rationale supported by visible evidence;
- trade-offs / consequences;
- unresolved assumptions or follow-up checks.

Do not invent a criterion merely because it would make the decision look cleaner.

## Recipe / reference card

Use for small, copyable operational patterns:

- command sequences;
- config fragments;
- prompt patterns;
- API call shapes;
- checklist fragments.

Parameterize environment-specific values, for example `<PORT>`, `<PROJECT_DIR>`, or `<MODEL_NAME>`.

## Retrospective

Use when the value is about how the work was approached rather than only the domain result.

Capture:

- what changed from the initial plan;
- which checks or decisions saved time;
- which approaches produced avoidable work;
- what should be done earlier next time;
- what remains context-specific and should not be generalized.

## FAQ

Use only when the conversation naturally contains recurring questions with stable answers. Do not manufacture FAQ entries from every paragraph.

## Modular bundle

Use when at least two artifact types carry independent long-term value or the conversation spans multiple subproblems.

Recommended shape:

```text
<slug>/
├── index.md
├── learning-note.md       # optional
├── playbook.md            # optional
├── troubleshooting.md     # optional
├── decisions.md           # optional
├── recipes.md             # optional
└── source-notes.md        # optional, only when provenance is useful
```

`index.md` should explain what the bundle teaches and link only to files that actually exist.
