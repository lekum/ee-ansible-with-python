# Ansible module example: `taiga_issue`

This example shows the usage of the `taiga_issue` custom module. The module is included in the `./library` folder.

In order to test it in you own Taiga.io hosted project, you need to:

- Have the python pre-requisites installed: `pip install -r requirements.txt`. If you install `python-taiga` in a virtualenv and not globally, specify the path to the python interpreter of the virtualenv in a host variable of the host. For example, in an inventory file it could be:

  ```
  localhost ansible_python_interpreter="~/.virtualenvs/ansible-taiga-issue/bin/python" ansible_connection=local
  ```

- Have credentials in environment variables. Authentication can be token-based or user/password based:
  - `TAIGA_TOKEN`
  - `TAIGA_USERNAME` and `TAIGA_PASSWORD`

- Replace the `YOUR_PROJECT` placeholder in `playbook.yml` for the name of your Taiga.io project.

Running the playbook:

```
ansible-playbook -v playbook.yml -i localhost, -c local
```

will create an issue, stop for up to a minute so that you can check it, and the continue and delete it.

If you are using an inventory file (e.g. you have installed `python-taiga` in a virtualenv), specify the path to the inventory file using the `-i` option.
