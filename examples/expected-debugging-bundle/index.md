# Local service reachable only after manual debugging

## Reusable lesson

When a service appears “down” after reboot, separate **process startup** from **network reachability** before changing service-manager configuration.

The shortest diagnostic chain is:

1. confirm the process/service is actually running;
2. inspect the listening socket and port;
3. inspect the bind address;
4. only then move outward to firewall, routing, or proxy layers.

In the example session, the service manager was already doing its job. The decisive evidence was a listener on `127.0.0.1:8080`, which showed that the application was restricted to loopback. Changing the application's bind address solved the remote reachability problem.

See [playbook.md](playbook.md) for the reusable procedure.
