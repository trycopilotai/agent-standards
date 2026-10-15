# Code Review Comments

Resolve a review thread after verifying that its finding is
addressed. Do this in the same pass as the fix. A pushed
commit alone does not tell the reviewer whether the finding
was handled.

If the fix landed somewhere unexpected, reply with the
relevant commit, file, or pull request before resolving the
thread. Use the hosting service's supported
thread-resolution operation rather than treating a comment
reply as closure.

Resolve exactly the findings you addressed. An outdated
annotation means the lines changed; inspect the current
behavior before deciding that the finding no longer applies.
Do not bulk-resolve findings based on outdated status alone.

A merge does not prove that every finding was fixed. Report
remaining findings by severity, with a concrete location and
the condition that triggers each one. Keep proposed changes
separate from verified defects.
