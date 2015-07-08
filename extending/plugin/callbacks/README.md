# Ansible callback plugin example: `notify_send`

This example shows the usage of a callback plugin.

To test it, run:

```
ansible-playbook -v playbook.yml -i localhost, -c local
```

If you are using a system that supports [notify-send](https://developer.gnome.org/libnotify/) command, it should show you a notification with the playbook failure.
