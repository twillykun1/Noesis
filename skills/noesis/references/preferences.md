# Private communication preferences

Read this when saving, correcting or retrieving a lasting explanation preference. These instructions describe storage; they do not grant permission to change user files or make private data safe to publish.

## What to retain

Store the actionable preference, its scope, a brief source and date. Keep it short: “Unfamiliar technical choices: start with a relevant example; user explicitly requested future use; YYYY-MM-DD.” This is an example, not this user's preference. Do not store a transcript, a competence/personality label, or a fixed learning type.

Reuse a matching item. A lasting correction replaces or removes its obsolete part; a one-time override leaves it intact. Preserve unrelated records. Read back the changed record before reporting success. Failed or uncertain writes are not saves; failed reads do not prove a record never existed. Keep personal content out of installed skill packages, project records and published artifacts.

## Codex: concrete user-level location

This route applies only to Codex environments that support user-level AGENTS instruction files and permit access to a private local home.

1. Resolve the actual Codex home: `CODEX_HOME` if configured; otherwise the current user's `~/.codex`. Do not assume another executor, profile or device has the same home or files. Resolve links and check the destination is private, outside the skill installation and shared/publishable repositories. A project-local `CODEX_HOME` is not a private preference destination.
2. The default record is a small `## Noesis communication preferences` section in `<Codex home>/AGENTS.md`. Reuse an existing matching preference section rather than creating duplicates. Do not replace the whole file or unrelated instructions. If the file does not exist, create it only when the user's save request and host permissions allow it.
3. Codex loads the first non-empty global file in this order: `<Codex home>/AGENTS.override.md`, then `<Codex home>/AGENTS.md`. An active override shadows the base file. If the active file already holds the preference, update that item. If preferences are in the shadowed file, do not silently duplicate, migrate or delete them: explain the conflict and ask which existing file the user wants maintained. Do not create/remove an override to force loading. If no preference exists and a non-empty override is active, confirm the intended lasting record before writing; an override may be temporary.
4. At the next relevant task or topic change, use applicable preferences already in context; otherwise read the relevant section from the confirmed active user file. A native Codex run normally assembles these instructions at startup, not on every turn. New file contents may require a new run or an explicit read. A successful save does not prove future model compliance; context limits, later instructions and unavailable files can affect use.

Default examples: macOS/Linux `~/.codex/AGENTS.md`; native Windows `%USERPROFILE%\.codex\AGENTS.md`; WSL uses its Linux home. `CODEX_HOME` overrides these defaults. These are local/profile-specific paths, not automatic synchronization or a universal location for every assistant.

## Other hosts or unavailable storage

Use the host's established authorized private preference/memory mechanism and documented retrieval route. Do not invent a local path or manipulate undocumented internal memory databases. If none is available, stay conversation-local and explain that limit when the user asks to remember. Do not create storage infrastructure or change global permissions to make persistence work.
