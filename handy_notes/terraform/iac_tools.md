## Categories ##

IaC tools can be broadly classified into three based on the specific purpose they are designed for.

### 1. Configuration management ###
* Eg: Ansible, Puppet, SaltStack
* Designed to install and manage software on existing infrastructure resources
* They maintain a consistent and standard structure of code
* Designed to run on multiple remote resource at once
* Can be checked into a version control repository
* They are idempotent, ie you can run the same script multiple times and it will only make changes that are necessary to bring the environment to a desired state

### System templating ###
* Eg: docker, vagrant, hashicorp packer
* Can be used to create a custom image of a virtual image or a container
* Pre-installed packages and dependencies
* Promotes immutable infrastructure

### Provisioning ###
* Eg: Terraform, CloudFormation
* Provision infrastructure using a simple declarative code
