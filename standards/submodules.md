# Submodules

A submodule's content and its consumer's gitlink are changes
in different repositories. Follow the dependency's own
instructions when editing its content. Avoid reformatting
vendored code under the consumer's unrelated style rules.

Commit and publish authorized dependency content first.
Verify that the intended consumers can fetch its exact
commit before committing the updated gitlink. A gitlink
records committed state; it cannot carry uncommitted edits.

Inspect dirty submodule content before advancing a pointer.
Do not hide unrelated edits with a pin bump. Register a new
dependency's URL, path, and gitlink together and verify them
from a fresh checkout.

Initialize only dependencies required by the task unless the
operator requests a full setup. Honor declared pins and
document the selected and skipped dependencies. A path-based
dependency scan can over-include entries; do not describe it
as a precise target build graph.

Use relative targets for authored symlinks. Check the stored
target and test resolution in a fresh clone. Tool-generated
workspace links follow their owning tool's contract.

Before removing a dependency, inspect local content and
commits, preserve required work, and update its declaration
and consumer references in the same reviewed change.
