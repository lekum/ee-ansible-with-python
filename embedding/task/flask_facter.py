from ansible.runner import Runner
from ansible.inventory import Inventory
from flask import Flask
from flask_restful import Resource, Api

class AnsibleFactResource(Resource):
    """
    A read-only local ansible fact
    """

    def __init__(self):
        self.facts = None
        Resource.__init__(self)

    def get_local_facts(self):
        """
        Loads the Ansible local facts in self.facts
        Calls the Ansible Python API v1 'setup' module
        """
        inventory = Inventory(["localhost"])
        runner = Runner(module_name='setup', module_args='',
                               pattern='localhost', inventory=inventory,
                               transport="local")
        result = runner.run()
        self.facts = result["contacted"]["localhost"]["ansible_facts"]

    def get(self, fact_name):
        """
        Returns a fist-level fact (not nested)
        """
        self.get_local_facts()
        try:
            return self.facts[fact_name]
        except KeyError:
            return "Not a valid fact: %s" % fact_name

app = Flask(__name__)
api = Api(app)
api.add_resource(AnsibleFactResource, '/facts/<string:fact_name>')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
