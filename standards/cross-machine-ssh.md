# Cross-Machine SSH

Read the operator's machine inventory and transport contract
before choosing a host, account, or route. Use the existing
connection helper when one is documented. Do not invent an
account from a device name.

Diagnose the failing stage: network reachability, access
policy, SSH service, host identity, client key, account
authorization, or remote command. Connection success alone
does not prove that the requested command succeeded.

Keep strict host-key verification. Verify a fingerprint
through an already trusted channel or local console before
trusting it. A network key scan alone proves no identity.
Investigate a changed fingerprint before replacing a pin.

Each source machine owns its private key. Enroll only its
public key through authorized access. Never copy a private
key or turn on agent forwarding to simplify enrollment. Keep
passwords in an interactive secret prompt or memory; never
put them in flags, files, logs, or Git.

Retest enrollment with a fresh connection so an existing
control socket cannot hide broken authentication. Verify
remote identity, exit status, and an appropriate round trip.

Preserve raw bytes during transfers. Avoid a PTY or text
pipeline for archives and transcripts. Check byte counts or
hashes, replace destinations atomically, and inspect the
destination before retrying an uncertain completed upload.
For durable jobs, read [WSL Offload](wsl-offload.md).
