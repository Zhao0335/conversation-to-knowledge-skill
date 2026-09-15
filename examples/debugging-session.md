# Example debugging conversation

User: My local dashboard works after I start it, but after reboot the browser says connection refused. I keep running the app manually again.

Assistant: First distinguish “service did not start” from “service started but is listening somewhere unexpected.” Check the service state and then check listening sockets.

User: `systemctl status dashboard` says active (running). `ss -ltnp | grep 8080` shows `127.0.0.1:8080`.

Assistant: That means startup is working. The next question is where the browser runs. If the browser is on another machine, binding only to loopback makes the service unreachable remotely. Check the app's bind/host setting.

User: The config says `host = 127.0.0.1`. I changed it to `0.0.0.0`, restarted the service, and now another machine can open it.

Assistant: Good. The root cause was not systemd startup but interface binding. Keep the distinction in your runbook: process state, listening socket, bind address, then firewall/routing if the socket is correct.

User: I had spent time reinstalling the service unit before this.

Assistant: Reinstalling the unit could not fix a process that was already active and listening on the wrong interface. The state/socket split is the faster diagnostic branch.
