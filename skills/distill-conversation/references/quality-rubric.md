# Quality rubric

Use this after drafting. The goal is not perfect prose; it is durable transfer.

Score each dimension 0, 1, or 2.

## 1. Fidelity

- **0** — important claims are invented, conflated, or contradict the source.
- **1** — mostly faithful but fact/inference boundaries are blurry.
- **2** — confirmed facts, user statements, observed results, and inference are clearly distinguished.

## 2. Reusability

- **0** — output only recounts what happened.
- **1** — contains reusable steps but remains tied to the original environment.
- **2** — extracts general patterns, parameterizes incidental details, and states when they apply.

## 3. Explanation

- **0** — gives conclusions without mechanism or rationale.
- **1** — explains some choices but misses key discriminators.
- **2** — explains why the method works, what evidence supports it, and why nearby alternatives fail or differ.

## 4. Actionability

- **0** — a future reader still needs the original transcript.
- **1** — most steps are actionable but important prerequisites or verification are missing.
- **2** — the artifact can be used independently, including entry conditions and success checks where relevant.

## 5. Boundaries

- **0** — overgeneralizes from one session.
- **1** — contains caveats but not the key failure conditions.
- **2** — states meaningful constraints, exceptions, and “do not apply this when…” guidance.

## 6. Failed-path value

- **0** — either deletes all failed approaches or repeats all of them indiscriminately.
- **1** — keeps failures but does not explain what they teach.
- **2** — keeps only failures that expose a useful branch, anti-pattern, or diagnostic signal.

## 7. Privacy and portability

- **0** — includes secrets or unnecessary identifying/environment-specific details.
- **1** — no obvious secrets, but portability is weak.
- **2** — sensitive details are removed/generalized and reusable values are parameterized.

## 8. Information density

- **0** — bloated, repetitive, or template-driven.
- **1** — useful but contains avoidable duplication.
- **2** — every section changes understanding or future action.

## Acceptance target

Aim for at least **12/16** overall with no zero in Fidelity or Privacy and portability.

Do not game the score by adding more sections. Revise the weakest dimensions with the smallest necessary change.
