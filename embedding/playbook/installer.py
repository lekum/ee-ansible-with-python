import sys
from getpass import getpass

from ansible.playbook import PlayBook
from ansible.inventory import Host, Inventory
from ansible import callbacks
from ansible import utils

def run_installer(user_list, package_list, sudo_password):
    """
    Runs the playbook `installer.yml` with the supplied parameters
    """

    # Create the inventory
    controller = Host(name = "localhost")
    controller.set_variable('users', user_list)
    controller.set_variable('apt_packages', package_list)
    local_inventory = Inventory([])
    local_inventory.get_group('all').add_host(controller)

    # Boilerplate for callbacks setup
    utils.VERBOSITY = 0
    # Output callbacks setup
    output_callbacks = callbacks.PlaybookCallbacks(verbose=utils.VERBOSITY)
    # API callbacks setup
    stats = callbacks.AggregateStats()
    api_callbacks = callbacks.PlaybookRunnerCallbacks(stats, verbose=utils.VERBOSITY)

    provision_playbook = PlayBook(playbook = "installer.yml",
                                  stats = stats,
                                  callbacks = output_callbacks,
                                  runner_callbacks = api_callbacks,
                                  inventory = local_inventory,
                                  transport = "local",
                                  become_pass = sudo_password
                                 )
    playbook_result = provision_playbook.run()
    return playbook_result

def get_selection_list(initial_prompt, input_prompt, continue_prompt):
    """
    Return a selection list chosen according to a flow described by:
        - initial_prompt: To enter the selection menu
        - input_prompt: To enter an item
        - continue_prompt: To continue entering another item
    """
    results = []
    enter_selection = raw_input(initial_prompt)
    enter_selection = True if enter_selection in ["y", "Y", "yes"] else False
    if enter_selection:
        while True:
            current_result = raw_input(input_prompt)
            if not current_result:
                break
            results.append(current_result)
            continue_selection = raw_input(continue_prompt)
            continue_selection = True if continue_selection in ["y","Y","yes"] else False
            if not continue_selection:
                break
    return results


if __name__ == '__main__':

    packages = []

    print("")
    print("Automated installation script")
    print("=============================")
    print("")

    sudo_password = getpass("Enter sudo password:")

    users = get_selection_list(
                               "Create users? (y/N)",
                               "Enter username:",
                               "Add more users? (y/N)"
                              )

    print("")

    packages = get_selection_list(
                                  "Install packages? (y/N)",
                                  "Enter package name:",
                                  "Add more packages? (y/N)"
                              )

    run_installer(user_list=users, package_list=packages, sudo_password=sudo_password)
