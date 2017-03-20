# My ansible playbooks

## Install Ubuntu 16.04 LTS (`playbooks/system.install.yml`)

This playbook is for very basic system configuration, including OS installation itself.

## About OpenVPN (`openvpn.setup.yml`)

After OpenVPN setup we need to open port (1194) and do firewall settings:

- At the top of `/etc/ufw/before.rules`:

```
# START OPENVPN RULES
# NAT table rules
*nat
:POSTROUTING ACCEPT [0:0]
# Allow traffic from OpenVPN client to eth0
-A POSTROUTING -s 10.8.0.0/8 -o eth0 -j MASQUERADE
COMMIT
# END OPENVPN RULES
```

- Allow forwarding at `/etc/default/ufw`:

```
DEFAULT_FORWARD_POLICY="ACCEPT"
```

- Open port:

```bash
$ sudo ufw allow 1194/udp
$ sudo ufw allow OpenSSH
```
