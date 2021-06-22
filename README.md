# ACI-Ansible
Cisco ACI project. Main project documentation: https://confluence.visma.com/display/VITC/Cisco+ACI+Documentation  

Install
```
virtualenv -p python3.6 venv
. venv/bin/activate
pip install ansible
pip install jmespath
pip install pyopenssl
ansible-galaxy collection install cisco.aci -p ./collections/
```
