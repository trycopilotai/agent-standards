# WSL Offload

Choose the documented channel for the job: a build service
for builds, a general remote executor for one-shot commands,
a durable job runner for long work, and the active release
owner for production changes. Keep release authority with
one owner.

Validate the actual transport across Windows, WSL, and
nested shells. Preserve argument boundaries, stdin EOF,
binary bytes, stdout, stderr, and exit status. Avoid text
filters or extra shell expansion on binary transfers.

Use a durable session manager or job service whose survival
has been tested after the controlling connection ends.
Capture output to a retained log and write a completion
record with the command's exit status as the final step. A
live terminal session alone does not prove success.

For a cold remote checkout, transport the exact commits
using an authorized Git remote or bundle. Verify the source
repository and commit, initialize required pinned
dependencies, and provide only the secrets the job needs
through an approved secret channel.

Read completion records and fetch logs before reporting a
job's result. Verify output hashes for code or file
transfers. State platform-specific checks that remain
unverified. See [Cross-Machine SSH](cross-machine-ssh.md).
