# v0.4.0 verification — 2026-11-10

## Scope

Candidate based on upstream `36e577f4b37e7a2dc0cce00ead1afebfca337732`, retaining the existing bilingual README commit. No personal preference content is included. Tests use fictional fixtures; the user's real global instructions and installed skill are not modified.

## Reproducible checks

```sh
PYTHONDONTWRITEBYTECODE=1 python3 scripts/check_package.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
git diff --check
```

Observed: valid six-file package; all 7 tests passed without skips on macOS with Codex CLI 0.153.4 and the installed official skill-installer. Before adding the new reference, package/copy tests failed because `references/preferences.md` was missing; the completed package passed.

The 4 package/installer tests check file types, names, version, isolated relative references, exact temporary copying, refusal to overwrite, and rejection of unsafe sources/names. Installer acquisition is substituted with local source; this is not a remote download test.

The 3 native Codex checks run `codex debug prompt-input` with temporary `CODEX_HOME` values and fictional AGENTS markers. They confirm:

- A user preference appears in assembled model input; a later fresh process sees the changed record and preserves unrelated fixture guidance.
- A non-empty `AGENTS.override.md` shadows `AGENTS.md`.
- An empty override falls back to the base user file.

This renders startup input without calling a model. It proves the tested CLI's loading mechanism under an isolated custom home, not subsequent model compliance or every desktop/runtime version. Default paths and platform distinctions are documented from the [official AGENTS reference](https://learn.chatgpt.com/docs/agent-configuration/agents-md). Missing CLI/debug-command or installer produces explicit test skips, which must not be reported as passes.

## Behavioral samples

Independent read-only simulations compare concrete communication and storage scenarios. The prior candidate already handled four communication cases appropriately: experienced user, rejected analogy, urgent payment risk overriding example-first, and refusal to infer a fixed visual learning type. The new wording makes the intended behavior explicit; it is not evidence of measured improvement.

Final candidate: 10 independently simulated cases gave the expected scoped actions. Four communication cases used the user's demonstrated knowledge, replaced an unwanted analogy with a concrete mechanism/timeline, put an urgent payment decision before a saved example-first preference, and did not infer a fixed learning type. Six storage/context cases declined a public-repository CODEX_HOME, asked before resolving a shadowed preference file, proposed a minimal private record while preserving unrelated instructions, reported an uncertain write/read failure without a success claim or blind retry, stayed local without supported storage, and avoided repeated lookup when preferences were already supplied.

These are single read-only samples with explicit scenario facts, not actual user-memory writes or statistical comparisons. They did not establish an improvement over the baseline.

An independent final review inspected the complete diff and new files, including the privacy/permission boundaries, override handling, test claims and package contents. It reported no actionable significant issues. The only completion condition was replacing this report's pending-results placeholder, now done. Local links in new/changed Markdown and a targeted publication-content check passed.

## Limits

No quantitative effectiveness, user comprehension, repeated-sample reliability, model compliance, non-Codex host compatibility, native Windows/WSL behavior or cross-device synchronization claim follows from these checks. No personal-memory migration, live installation, global configuration change or release tag is part of this change.
