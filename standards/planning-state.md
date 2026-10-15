# Planning and State

Save an approved implementation plan in the repository's
documented plan store before implementation when its policy
requires this. Record context, decisions, target files,
validation commands, dependencies, and scope boundaries. Use
a new plan for new work and update the active plan when its
approved scope changes.

Treat task statuses as current state. Mark a step complete
only when the validation named in the plan has succeeded.
Record the command, result, or review artifact that supports
completion. Leave partially delivered steps in progress with
their remaining work explicit.

Keep routine task-state changes separate from unrelated
feature commits. Do not stage another task's incidental
changes. Keep an append-only transition record when the
repository requires an audit trail.

A handoff should identify the objective, current state,
decisions, exact artifacts, relevant commits, known
failures, and the next action. Separate verified results
from assumptions and pending work. Never mark a review
complete before its result arrives.

Store outbound drafts and retained evidence in their named
stores. If moving a live run directory, first stop its
writers; update references and regenerate all path-bound
hashes, signatures, and review receipts.

Persist only task-relevant durable preferences. Never place
personal context in public documentation merely because it
appeared in the working conversation.
