# Agent CLI Invocation

Use the repository's documented launcher and pinned tool
version. Inspect its help before relying on flags or output
formats. Keep the launch command reproducible in scripts and
handoff notes.

For a resume command, identify the exact session and working
directory. Avoid a last-session shortcut when it could
select another task. Verify the session identifier from
trusted runtime state rather than guessing one.

Permission controls are an operator decision. Preserve the
permissions authorized for the task; do not silently expand
them to make a headless command work. Record any limitation
that prevents a required check.

For a review, confirm whether the CLI permits a custom
prompt alongside a scope flag. Name the reviewed files or
commit explicitly. Read the final findings artifact and
process exit status; a streamed progress message is not a
completed review.

Keep provider credentials out of command arguments, logs,
and transcripts. Use the provider's supported credential
store.
