# Benefits, spending, and recovery

Read when account access, budgets, free/Unlimited benefits, or submission recovery affect the workflow.

## Capture the current policy

Extract a working policy from the user's request and existing project instructions:

| Field | Meaning |
| --- | --- |
| Task | Research, quote, generate, edit, or inspect an existing job. |
| Allowed free uses | Whether the user has allowed eligible free or Unlimited generations for this work. |
| Allowed paid uses | Output types and purposes that may consume existing credits. |
| Limits | Any per-job, batch, total, or remaining-allocation ceiling. |
| Inputs | Authorized references, their roles, and their upload destination. |
| Execution surface | Connected tools, website, API, or another explicitly supported route. |

Do not invent a numeric budget or interpret a visible balance as a target to spend. If paid use is authorized without a numerical cap, use the requested scope and exact quote; ask only when a material spending decision remains unresolved or a tool requires explicit confirmation.

Purchases, subscription changes, and publishing are separate actions. Do not infer authorization for them from permission to generate.

## Verify the benefit on the actual route

1. Read current balance and benefit state when needed. A one-off research request need not inspect unrelated account details.
2. Check the selected product, version, operation, resolution, output format, duration, and count. A still-image benefit may exclude animated output or vectors.
3. Check the actual channel. Account access on the website does not establish the same access through a connector or API.
4. Read counter scope and restrictions. Two operations can share one free counter; a character sheet allowance is not a general image allowance.
5. Record unverified details as unknown. A missing marker does not prove that a different channel has no offer.

Use explicit free/Unlimited selectors only when supported, currently eligible, and authorized. For example, some tools expose `use_free_gens`, `use_unlim`, or a maximum-credit field. These names are examples: use the current tool schema, not a fabricated request shape. Do not combine mutually exclusive benefit modes.

## Quote and submit

Quote the actual operation with the actual configuration and reference mode. Text-only and reference-driven modes can have different prices. A public pricing example, stale quote, or model-level credit rate is not a guaranteed submission price.

Cost-only estimates should omit remote references when the user has not requested their upload and the tool permits a reference-free quote. Some estimation tools import remote assets: inspect that behavior before sending URLs. A quote without required references remains a price estimate, not readiness validation.

If the user authorized free/Unlimited only, a rejected benefit request stops that execution path. Do not retry it with credits. If paid use is also authorized, reassess that policy and quote the paid operation before submitting; never change the payment route silently.

Keep an approved exact allocation unchanged through any required tool approval. Requote changed parameters or material price changes and follow the tool's rules. Preserve prior authorization when scope and conditions remain the same.

## Recover without duplicate work

- On a definitive input rejection, correct the specific input and revalidate; do not repeatedly resend an unchanged request.
- On timeout or a lost response, the submission outcome is unknown. Inspect known jobs or use supported idempotency recovery before trying again.
- Reuse an existing job/result for status and display. Do not regenerate to obtain another preview widget.
- If neither job lookup nor idempotency can determine the outcome, stop resubmission and report that exact uncertainty.
- Follow supported polling intervals. Report a terminal failure and its reason; do not keep regenerating until credits run out.

## Minimal execution record

Use a small record appropriate to the project rather than a mandatory database:

```text
task / intended use
model and operation
parameters and reference roles
execution channel and benefit evidence
quoted cost / actual cost if reported
job ID and submission state
accepted result / local or supported result location
```

Keep private account data and reference URLs in the authorized project context, not in the distributable skill.
