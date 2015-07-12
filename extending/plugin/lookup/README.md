# Ansible lookup plugin example: `shelvefile`

This example shows the usage of a lookup plugin. The plugin reads a key from a [shelve](https://docs.python.org/2/library/shelve.html#module-shelve) file.

To test it, run:

```
ansible-playbook -v playbook.yml -i localhost, -c local
```
