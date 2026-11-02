# Trace only what can change this decision

Use this reference when a consequential choice crosses modules or services, or available evidence conflicts. Build the smallest causal trace that could change the recommendation. Begin at the changed behavior and inspect relevant callers, downstream consumers (including asynchronous workers), effective deployment configuration, data sources and failure paths. Follow discovered references; do not exhaustively inventory the repository.

For each important link, identify the observed code/configuration or contract and its revision/environment. Separate what it establishes from what you infer. Search results establish only what was searched: “no consumer found in these directories” does not mean “no consumer exists.” Check event subscriptions, deployment manifests or interface contracts when relevant to that gap.

Translate the trace into a concrete consequence: a stale display value reused at checkout changes what a customer pays; an acknowledged payment followed by a lost response can make a retry charge twice; a queued notification can still be sent after code rollback. Tests proving a local return value may not cover these outcomes.

If a key external system or configuration is inaccessible, state the accessible coverage, missing fact and how it affects the recommendation. Offer a conditional recommendation and the evidence needed to remove the condition. Do not promise end-to-end safety. Pause the affected high-risk action, such as enabling payment retries, while continuing independent authorized investigation, implementation or tests. Ask the user only for an indispensable value choice or permission, not to research technical facts on your behalf.

When configuration, contracts or code change, recheck the relevant links and acceptance evidence before reusing a previous conclusion. Distinguish reverting code from reversing reality: money already moved, messages delivered and data removed may require reconciliation, compensation or may be irreversible. State that limit in the recommendation and acceptance criteria.

Stop expanding the investigation when the decision-changing premises have sufficient evidence, or when a clearly described access limit prevents resolution. Summarize the recommendation, human consequence, cost and remaining condition; keep supporting technical detail available rather than burying the decision in a dependency inventory.
