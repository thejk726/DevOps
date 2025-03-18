## AWS CloudFormation ##

* `AWS CloudFormation` is a service that helps you model and setup your AWS resources.
* Using CloudFormation, all the user need to do is to create a CloudFormation template that describes all the required AWS resources and CloudFormation is going to take care of provisioning and configuring the specified resource.
* Both `json` and `yaml` formatted template files are supported.
* When you define resources in a template, you'll be grouping them into `stacks`, which are managed single units within CloudFormation. Stacks allow creation, updation and deletion of resources as a group.
* Once the stack is created, it'll go and provision all the resources that are defined within it.
* When updating the environment, first we have to edit the template, update the stack and pass it to CloudFormation . CloudFormation then updates the `change set` which allows you to preview how proposed changes to a stack will impact your resources by comparing the current deployed resources and the updated template before applying the changes.

## Features and benefits ##

1. It's infrastructure as code (IAC).
   * It allows for version control, thereby allowing us to track changes made to the infrastructure.
   * It allow us to utilize other AWS services like `AWS CodeCommit` which is the managed service for version control to track the IaC code and `AWS CodePipeline` and `AWS CodeBuild` to build and provision the infrastructure.

2. Consistent and repeatable deployments.
   * Deployment across multiple environments for instance.
   
3. Resource tracking. 
   
4. Cost and time efficiency
   * Faster alternative to mannual provisioning and configuration.

