# Disk Cleanup

Treat agent transcripts, session archives, run records, and
logs as retained history. Do not propose deleting them as a
routine disk-space remedy. Archived history remains history.
If only retained history remains, report that limitation.

Look for rebuildable caches and provably orphaned build
state first. Read a candidate before classifying it. A
directory named cache may contain the executable that a live
agent is using.

Check for running processes, open files, current working
directories, and active build servers before removing state.
Preserve browser profiles and caches held by running apps.
Map each build output directory to its owning workspace; do
not start a build tool merely to discover an output path if
doing so would create more state.

Before removing a worktree, inspect tracked changes,
untracked and ignored files, nested repositories, submodule
changes, registered child worktrees, and commits absent from
remote history. A clean status alone is insufficient.

Preserve anything not independently recoverable. Use Git's
worktree removal command after verification, from outside
the tree. Do not automatically prune worktree registrations.
Remove associated build state only after separate checks for
live consumers. See
[Worktree Lifecycle](worktree-lifecycle.md).
