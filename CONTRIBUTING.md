# Contributing

Contributions are welcome when they improve observable behavior rather than merely adding more prompt text.

## Principles

- Keep the installable skill small. Repository documentation belongs outside `skills/distill-conversation/` unless the agent needs it at runtime.
- Prefer a deterministic script for repetitive parsing or validation work.
- Prefer a reference file for detailed semantic guidance that does not need to be loaded every run.
- Do not add rules for a single anecdotal failure unless the failure reveals a generalizable defect.
- Never add fixtures containing real secrets, personal data, private infrastructure names, or hidden system/developer prompts.

## Test

```bash
python -m unittest discover -s tests -v
```

For semantic changes, also run the cases in `evals/cases.yaml` manually or through your preferred agent-evaluation harness and record whether the expected properties hold.

## Pull requests

Explain:

1. the failure mode or missing capability;
2. the smallest change that fixes it;
3. how you verified the change;
4. whether the change affects triggering, privacy, source fidelity, or output structure.
