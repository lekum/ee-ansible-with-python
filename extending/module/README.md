# Ansible module example: `taiga_issue`

This example shows the usage of the `taiga_issue` custom module. The module is included in the `./library` folder.

In order to test it in you own Taiga.io hosted project, you need to:

- Have credentials in environment variables. Ths is, either:
  - `TAIGA_TOKEN`
  - `TAIGA_USERNAME` and `TAIGA_PASSWORD`

- Replace the PROJECT placeholder in `playbook.yml` for the name of your Taiga.io project.

Running the playbook:

```
ansible-playbook -v playbook.yml -i localhost, -c local
```

will create an issue, stop for up to a minute so that you can check it, and the continue and delete it.
