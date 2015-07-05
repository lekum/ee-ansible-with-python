import sys

from ansible.playbook import PlayBook
from ansible.inventory import Host, Inventory
from ansible import callbacks
from ansible import utils

def provision_ec2_instance(ec2_hostname, ec2_ami_id):

    # Create the inventory
    controller = Host(name = "localhost")
    controller.set_variable('ec2_hostname', ec2_hostname)
    controller.set_variable('ec2_ami_id', ec2_ami_id)
    local_inventory = Inventory([])
    local_inventory.get_group('all').add_host(controller)

    # Boilerplate for callbacks setup
    utils.VERBOSITY = 0
    # Output callbacks setup
    output_callbacks = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    # API callbacks setup
    stats = callbacks.AggregateStats()
    api_callbacks = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

    provision_playbook = PlayBook(playbook = "provision_ec2_instance.yml",
                                  stats = stats,
                                  callbacks = output_callbacks,
                                  runner_callbacks = api_callbacks,
                                  inventory = local_inventory,
                                  transport = "local"
                                 )
    playbook_result = provision_playbook.run()
    return playbook_result

if __name__ == '__main__':

    ec2_hostname = sys.argv[1]
    ec2_ami_id = sys.argv[2]
    print(provision_ec2_instance(ec2_hostname, ec2_ami_id))
