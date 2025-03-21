## Terraform ##
* Free and open source nfrastructure provisioning IaC tool developed by HashiCorp
* Enables infrastructure provisioning and deployment across multiple platforms, both on-premise and cloud
* `Providers` help terraform manage third party platforms through their API
* It uses HCL ( HashiCorp configuration language )
* All infrastructure resources can be defined as blocks of code in configuration files with a `tf` extension
* The code is declarative and can be checked to a VCS

## Terraform execution phases ##
* `init` - In this phase, terraform identifies the project and identifies the providers to be used for the target environment.
* `plan` - In this phase, terraform drafts a plan to get to the desired state.
* `apply` - In this phase, terraform makes the required changes to bring the environment to the desired state.

#### NOTE ####
If for some reason, the environment was to shift from the desired state, a subsequent apply will bring it back to the desired state by only fixing the missing component.

* Every object that terraform manages is called a resource.
* Terraform manages the lifecycle of a resource from provisioning to configuration to decommisioning.
* It keeps a record of the infrastructure as it is seen in the real world and based on this, it can decide what actions to take when updating resources for a particular platform.
* Terraform can read the attributes for existing infrastructure resources by configuring `data sources`. This can later be used for configuring other resources within terraform.
* Terraform can also import resources outside of terraform that were either created mannually or by means of other IaC toolsand bring it under it's control so that it can manage them going forward.
* 
