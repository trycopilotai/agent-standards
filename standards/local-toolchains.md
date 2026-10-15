# Local Toolchains

Start with the repository's documented build and validation
path. Inspect existing executables, caches, package
managers, and version pins before installing another
toolchain.

When the preferred runtime fails, identify the failing layer
and repair it within the authorized scope. Rerun the
original command after the repair. Do not silently skip a
required check because the first invocation failed.

If that runtime remains unavailable, use a compatible local
toolchain with the declared versions. State which checks it
can reproduce and which remain untested. Treat a successful
subset as evidence for that subset only.

Prefer project-local or user-scoped installs. Obtain the
operator authorization required for privileged or material
system-wide changes.

Use the operating system's supported application launcher to
open a GUI app or file. Use GUI automation when the task
requires interacting with controls or reading live UI state.
A GUI launcher and an agent's command-line launcher are
different interfaces; verify the intended one.
