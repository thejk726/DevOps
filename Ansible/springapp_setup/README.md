# 🌟 Ansible Project: Automated Infrastructure Provisioning and Deployment

## 📈 Overview

This project automates the provisioning and deployment of a complete infrastructure using Ansible. It includes modular roles that handle tasks such as Java installation, Spring Boot application deployment, MySQL setup, and Python module management. The project’s structure is designed for easy reuse, scalability, and adaptability across different environments.

## 📂 Project Structure

```plaintext
├── ansible.cfg               # Ansible configuration file
├── deploy.yml                # Playbook for application deployment
├── inventory/                # Inventory files for different environments
│   └── dev/
│       ├── group_vars/
│       │   ├── dev.yml       # Variables for the dev environment
│       │   └── secret.yml    # Encrypted secrets
│       ├── hosts             # List of hosts in the dev environment
│       └── host_vars/
├── provision.yml             # Playbook for provisioning infrastructure
├── README.md                 # Project documentation
└── roles/                    # Directory containing all Ansible roles
    ├── deploy/
    ├── java_install/
    ├── mysql_install/
    └── python_modules/

