#!/usr/bin/python3
from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(argument_spec={})
    data = {
        "message": "Custom info module works!",
        "author": "Student"
    }
    module.exit_json(changed=False, info=data)

if __name__ == '__main__':
    main()
