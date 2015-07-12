# Dynamic Inventory Script example: `shelve_inventory`

This is an example of a dynamic inventory script for Ansible. The script reads the groups, hosts and vars information from a [shelve](https://docs.python.org/2/library/shelve.html) file.

The shelve file path can be specified in the `defaults` section of the `shelve_inventory.ini`:

```
[defaults]
shelvefile = inventory.db
```

The script `create_inventory.py` populates an example of shelve inventory. This will run a demo with this inventory:

```
ansible-playbook -v playbook.yml -i shelve_inventory.py -c local
```
