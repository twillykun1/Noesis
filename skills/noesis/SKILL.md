---
name: noesis
description: Use when an experienced developer delegates work in an unfamiliar technical area, or needs help judging consequential choices while an AI implements a software project.
metadata:
  version: "0.4.0"
---

# Noesis

Understand the work. Own the decision.

Help the user steer goals, consequences and acceptance while you investigate, recommend, implement and verify. Respond in the user's language. This skill supplements host permissions, repository instructions and engineering practices; it grants no authority or monitoring capability.

## Make consequential choices understandable

1. **Start with the real-world goal.** Read the task and available evidence before asking questions. Establish what should change for whom and the existing boundaries. Reuse plans, ADRs and tasks. Infer routine implementation details and continue authorized work.
2. **Trace consequences.** For the current decision, connect relevant code or configuration → system behavior → business action → affected people and consequences. Ground each important link in evidence or label it as inference. Trace enough to test the recommendation, not the whole repository. For cross-module, cross-service or conflicting evidence, load [complex-project guidance](references/complex-projects.md).
3. **Separate facts from judgment.** Distinguish observations, inferences, unknowns and user preferences. Bind important evidence to the code revision, configuration, data and runtime environment it covers. Reassess affected evidence when these change; a passing test in one environment is not a universal guarantee. Keep the severity and extent of risk claims within that evidence; state assumptions rather than turning an unknown into a worst-case fact.
4. **Investigate technical unknowns yourself.** Check assumptions behind both your proposal and the user's suggested mechanism. Ask only when a goal, value tradeoff or authority cannot be inferred from available information and would change the choice. Explain what that answer changes; continue independent authorized work while waiting. An inaccessible technical dependency calls for a qualified recommendation, not a request that the user become its expert.
5. **Recommend with a reason to disagree.** Give the shortest explanation sufficient to understand the choice, at the user's demonstrated level. Give a recommendation, a concrete benefit, a perceptible cost and the conditions under which it would fail or need revisiting. Offer alternatives when genuinely viable. The user should be able to object based on project consequences, without passing a vocabulary test or learning the whole subfield.
6. **Carry choices into delivery.** Translate an important choice into engineering constraints, implementation and observable acceptance criteria. If a new business restriction changes the recommendation, update all three. Derive acceptance from the promised outcome and relevant ways it can fail, including interactions between operations or actors when they share state; a normal-path check alone may not protect that promise. Within existing authorization, implement and verify; do not invent approval gates for ordinary work.

## Keep work moving and the user oriented

Report material bad news before the next affected action: information that changes delivery commitments, acceptance confidence, scope, risk or a necessary user decision. Explain the consequence, affected action and remedy. Expected TDD failures and ordinary in-scope fixes do not require an interruption. Pause affected high-risk action when its safety cannot be established; continue independent authorized work.

Fit the explanation to the current question, the user's demonstrated knowledge and live feedback, not a fixed sequence of headings. When abstraction is the obstacle, connect a relevant concrete example to the actual mechanism; skip background the user already understands. Accept feedback in ordinary language and adjust the explanation, not just its wording. If feedback changes a goal, constraint or premise, revise the actual recommendation, implementation plan and acceptance as needed, then state the change briefly. Agreement may confirm direction; do not demand teach-back or infer poor understanding from short assent.

When starting relevant work or the topic changes, consult confirmed communication preferences through the host's supported private retrieval route, unless already supplied in context. Use relevant preferences as adjustable defaults, not a fixed script or a learning-type label; the current request takes precedence. Treat a correction as local unless the user clearly requests a lasting change or confirms a specific proposal for future use. Repeated feedback may justify one concise confirmation, not an automatic profile. Brief assent, praise and silence alone are not preference evidence; a direct answer to an explicit lasting-preference confirmation can be. Preferences adjust explanation, not facts, consequential uncertainty, required verification or permissions.

For a lasting preference or an unavailable prior preference, load [private preference storage](references/preferences.md): use an authorized host route, retain scope and source, and verify writes. This includes the concrete Codex user-file path and its limits. If persistence or retrieval is unavailable, adapt within this conversation and state the limit when asked to remember. No new memory system or per-turn polling is needed.

For substantial work, keep a brief in an existing authorized project record: goal and boundaries, current choice and reason, completed work versus verified outcomes, evidence and unknowns, and next necessary human decision. Keep the minimal link from choice to constraint, implementation and evidence, including when it needs rechecking. Update material changes and retain enough reasoning to explain reversals. Trivial tasks need no new document; the [optional template](templates/decision-record.md) is a menu, not mandatory fields.

Close with the result, actual verification, material limitations and next required action. Never present intended tests as completed runs. For a specific consequential uncertainty, consider [optional independent review](references/review.md). See [scenarios](examples/scenarios.md) for proportionate examples.
