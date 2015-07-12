#!/usr/bin/env python

import shelve

d = shelve.open("inventory.db")

db_group = {}
db_group['hosts'] = ["db1", "db2"]
db_group['vars'] = {"db_username": "root"}

web_group = {}
web_group['hosts'] = ["web1", "web2", "web3"]

production_group = {}
production_group['hosts'] = ["web1", "db1"]

hostvars = {}
hostvars['web1'] = {"ansible_ssh_host": "localhost", "engine": "apache", "engine_version": 2}

d['groups'] = {"databases": db_group, "web": web_group, "production": production_group}
d['hostvars'] = hostvars
d.close()
