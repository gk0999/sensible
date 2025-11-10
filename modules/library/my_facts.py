#!/usr/bin/python3
from ansible.module_utils.basic import AnsibleModule
import platform
import socket

def main():
    module = AnsibleModule(argument_spec={})
    facts = {
        "hostname": socket.gethostname(),
        "os": platform.system(),
        "release": platform.release(),
    }
    module.exit_json(changed=False, ansible_facts=facts)

if __name__ == '__main__':
    main()
