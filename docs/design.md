# Design notes

Long AI-assisted work sessions mix final results, successful steps, failed hypotheses, environment-specific noise, decisions, explanations, corrections, and transient logistics. A generic chronological summary flattens those categories and makes the result less reusable.

## Core transformation

The skill uses three semantic passes:

1. **Evidence pass** — identify the goal, constraints, actions, observed results, decisions, corrections, failed approaches, and final outcome.
2. **Durability pass** — separate reusable knowledge from session-only details and uncertain claims.
3. **Teaching pass** — transform durable evidence into learning notes, playbooks, diagnostic guides, decision records, recipes, or retrospectives.

## Design principles

- Do not invent rationale that the source does not support.
- Prefer reusable decision rules over chronology.
- Preserve failed paths only when they teach a useful branch or anti-pattern.
- Use templates selectively rather than forcing one schema onto every conversation.
- Keep semantic extraction in the model and deterministic parsing/validation in small scripts.
