# Worktree Lifecycle

A worktree belongs to a specific change. Record its owning
repository, purpose, base, branch, creation time, and
associated build state in the project's worktree inventory.
Keep canonical checkouts stable.

Use the repository's worktree helper and documented
placement. Keep retained inputs, outputs, logs, plans, and
reviews in durable named stores. Provider-owned runtime
directories and disposable scratch areas are not durable
artifact stores.

After a change lands, verify the worktree's status,
untracked and ignored content, nested repositories,
submodules, and commits. Check remote reachability or patch
equivalence when rebase-and-merge changed commit IDs. An
open pull request or unrecoverable work prevents retirement.

Check for processes whose current directory is in the tree
and for open files in associated build state. The agent's
own session may be a live consumer even after a shell
command changes directories.

Remove a verified finished worktree from outside it using
Git's worktree command. Inspect associated build state
separately before removing it. Never automatically prune
registrations or discard dirty content.

Update the inventory after retirement. A sweep must apply
the same preservation and live-consumer checks as manual
removal. Age alone is not evidence that a tree is safe to
delete. See [Disk Cleanup](disk-cleanup.md).
