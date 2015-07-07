# EC2 provisioner

This example shows how to embed a call to an Ansible playbook. The file `ec2_provisioner.py` defines a function named `provision_ec2_instance` that takes 2 parameters (`ec2_hostname`and `ec2_ami_id`) and runs a playbook named `provision_ec2_intance.yml` passing along the variables as host variables.

The playbook is just a mock: instead of creating the EC2 instance, it just displays a message with the values of the `ec2_hostname` and `ec2_ami_id` passed to the function.

In order to test it, issue:

```
python ec2_provisioner.py my_host my_ami_id
```

It should print something like this:

```
PLAY [localhost] **************************************************************

GATHERING FACTS ***************************************************************
ok: [localhost]

TASK: [This is a simulation message] ******************************************
ok: [localhost] => {
    "msg": "The hostname is my_host and the ami_id is my_ami_id"
}
{'localhost': {'unreachable': 0, 'skipped': 0, 'ok': 2, 'changed': 0, 'failures': 0}}
```
