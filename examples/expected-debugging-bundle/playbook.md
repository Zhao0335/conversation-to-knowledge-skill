# Playbook: service runs but cannot be reached remotely

## Symptom

A service reports as running, but clients on another machine receive connection failures.

## Diagnostic sequence

1. **Check process/service state.** If it is not running, stay in the startup branch.
2. **Check the listening socket.** Confirm that the expected port exists.
3. **Inspect the bind address.** A listener on `127.0.0.1:<PORT>` accepts only local connections; a listener on an appropriate non-loopback address is required for remote clients.
4. **If the bind address is correct, continue outward.** Check firewall policy, routing, reverse proxy, security groups, or container port publishing as applicable.

## Why this order works

Each step rules out an entire class of causes. It avoids changing the service manager when the process is already alive and narrows the problem from process lifecycle to application socket configuration before investigating broader networking layers.

## Anti-pattern

Do not reinstall or rewrite service-manager configuration merely because a remote client cannot connect. First verify whether the service is already running and where it is listening.

## Portable command pattern

```bash
systemctl status <SERVICE>
ss -ltnp | grep <PORT>
```

Substitute the service name and port for the target application.
