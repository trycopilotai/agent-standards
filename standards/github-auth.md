# GitHub Authentication

Use the repository's documented credential source and the
least access sufficient for the task. Read the configured
account and repository permissions before diagnosing an
authentication error.

Keep token values out of output, command arguments, remote
URLs, committed files, process traces, and retained logs.
Use a supported credential helper or an authenticated CLI
store. Never print a token to prove that it exists.

Separate missing authentication from insufficient repository
permission, organization authorization, and network failure.
Check the exact account, target repository, and operation.
Report the smallest missing authorization if trusted access
cannot complete the task.

For a publication transaction, isolate its credential store
and make credentials available only after the required
release authorization. Offline checks should run without
publication credentials or ambient authenticated helpers.
