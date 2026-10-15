# Checkout Guard

A checkout read by live tooling is a canonical checkout.
Keep it on its declared branch. Make branch changes in a
separate Git worktree so path-based consumers continue to
read the expected source.

Record the branch pin explicitly. Do not infer a branch from
a stale remote default or silently repair a pin by switching
the checkout. Audit detached and unexpected branch states.

Before installing a hook, inspect existing hooks. Preserve
their behavior and refuse to overwrite a hook owned by
another tool. A global hook directory can replace a
repository's existing hook lookup; account for that effect.

A local guard reduces accidental drift. It does not prevent
a deliberate bypass and does not replace a recurring audit.
Test branch-switch protection and worktree creation with the
Git version used by the repository before enforcing it.
