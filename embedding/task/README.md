# Flask facter

This example shows how to embed a call to an Ansible module (equivalente to perform and ad-hoc task). It uses [FlaskRESTful](https://flask-restful.readthedocs.org/) to spin up a very simple REST api to get the Ansible facts of the machine.

In order to test it, issue:

```
python flask_facter.py
```

And then, open a web browser and enter this url: [http://localhost:8000/facts/ansible_hostname](http://localhost:8000/facts/ansible_hostname). It should print your hostname.
