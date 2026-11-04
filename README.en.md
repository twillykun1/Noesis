# Noesis

[简体中文](README.md) | **English**

**Understand the work. Own the decision.**

Have AI translate code behavior into real-world consequences you can judge—and carry your decisions through to delivery.

You have development experience, but you cannot be an expert in every technical field. Noesis helps you steer direction, key risks, and acceptance when working outside your specialty. AI investigates, recommends, implements, and verifies. It supplies only the background needed to make a choice and keeps authorized work moving.

## From “which parameter?” to “who does this affect?”

Suppose you want a faster product endpoint:

| Discussing implementation parameters alone | Tracing project consequences with Noesis |
| --- | --- |
| “Let's add a 60-second cache. How much delay can you accept?” | “If inspection shows that checkout also reads this endpoint, caching could make customers pay an old price. I'll first confirm the bottleneck and call chain, then recommend how to improve speed while keeping checkout accurate.” |

Recommendations come with evidence, costs, and conditions that would invalidate them. Your choice becomes engineering constraints and acceptance criteria. This is an example of collaboration, not an effectiveness test result.

## Install with one sentence

Give your AI this request:

> Use your built-in skill-installer to install Noesis from https://github.com/twillykun1/Noesis/tree/main/skills/noesis; if it is already installed, explain the differences before updating.

Prefer the official Codex `skill-installer`. Install `skills/noesis`, not the repository root. For an existing installation, compare and back it up, then update after obtaining authorization to replace it. The sentence above describes an update process; it is **not an automatic updater**. Follow your host's instructions for installation location and reloading.

## Start using it

> Use Noesis to help me redesign login sessions. Inspect the current system first and explain the practical impact of key tradeoffs; keep authorized work moving.

You can also say “I don't understand,” “I disagree,” “too detailed,” or “unnecessary.” AI should adjust its explanation. If feedback changes a goal or constraint, it should also revise the approach, implementation, and acceptance criteria. Simple copy edits should be completed directly, without creating a decision document.

## How it works

- **Start with the goal**: establish whose experience or work should change, and how.
- **Trace consequences through code**: inspect relevant configuration, callers, and consumers; connect system behavior to business actions and the people affected.
- **Recommend with evidence**: separate facts, inferences, and preferences; explain benefits, costs, and changes in assumptions that would invalidate the recommendation.
- **Carry decisions into delivery**: connect important choices to engineering constraints, implementation, and observable acceptance criteria, separating work completed from outcomes verified.

The core instructions stay lightweight. Complex tasks load cross-module investigation guidance as needed. Important state belongs in an existing plan or ADR where possible, rather than a new table for every task.

## Validation and contributions

Current version: **v0.3.1**. The runtime consists of five Markdown files and is self-contained and independently installable. Maintenance checks cover package structure, relative references, temporary-directory copying with the official installer, and refusal to overwrite an existing installation. These checks do not demonstrate improved model behavior or human understanding. See the [maintenance guide (Chinese)](docs/maintenance.md) for commands, validation limits, and installation maintenance, and the [Changelog (Chinese)](CHANGELOG.md) for version changes.

Concrete cases are welcome: the task and necessary context, expected and actual output, missed consequences, or unnecessary intervention. Remove secrets, personal information, and private business material. Changes backed by inspectable evidence and a clear validation scope are more useful than simply adding rules.

The host still controls skill activation, permissions, and execution. Compatibility with other agents and native automatic discovery have not been verified. Historical materials remain in the repository but are not part of the current installation package. This repository does not yet include an open-source license; public visibility does not grant an open-source license to use it.
