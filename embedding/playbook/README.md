# Automated installation script

This example shows how to embed a call to an Ansible playbook.

It consists on an interactive script that will ask you for your sudo password and a list of users to be created in the system and apt packages to be installed. Finally, it runs the playbook `installer.yml` supplying these values as inventory variables.

In order to run it, type:

```
python installer.py
```

and follow the on-screen instructions.
