# Pull Request Merges

This standard adopts rebase-and-merge to retain the authored
commit sequence and a linear default branch. Split
mechanical changes from semantic ones and order commits for
human review. A team adopting another policy should state
its choice explicitly in its own instructions.

Inspect the pull request's exact head, base, checks, review
state, and merge permission before landing it. Follow the
operator's authorization and repository publication policy.

When bringing a branch up to date, rebase it onto its base.
Resolve conflicts and rerun the affected checks. Do not
silently fall back to a different merge method when the
required one fails.

If an authorized branch rewrite is necessary, inspect the
remote head first and use a lease-protected update. Never
overwrite a released tag or shared history as an ordinary
repair. New publication transactions should push only their
reviewed refs.

After landing, verify the resulting default-branch state,
resolve findings actually addressed, and retire the finished
branch and worktree under
[Worktree Lifecycle](worktree-lifecycle.md).
