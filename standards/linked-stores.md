# Linked Stores

Keep a documented map from logical artifact types to their
canonical stores. Plans, exports, transcripts, logs, working
files, and runtime locks have different retention and access
requirements. Resolve the map before inventing another path.

A compatibility symlink is an alias, not a second store.
Resolve its actual repository before editing, staging, or
committing. Check whether a path is a symlink, directory,
worktree, or submodule before treating it as one.

Keep authored symlink targets relative and portable. Verify
the stored target with readlink. Avoid staging a
materialized copy of a symlink as a directory or
accidentally recording a nested repository as a gitlink.

Commit content in its owning repository before advancing
consumer pointers. Ensure the referenced commit is reachable
to intended consumers. See [Submodules](submodules.md) for
the content-then-pointer sequence.

Retain audit artifacts in durable private storage. Keep
credentials and rebuildable runtime caches outside committed
artifact bundles.
