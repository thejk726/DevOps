## NAT Gateway ##

The goal behind a NAT gateway is to provide internet access to a resource within a subnet (private) only if the connection is initiated from within the VPC and not from the internet.

#### NOTE ####

Nat Gateways are in no way an alternate to an IGW. In fact, it needs an IGW to work.

## How it works? ##

To enable internet access to a resource in the private subnet in the above manner, the following should be the procedure - 

* Deploy a NAT Gateway in the public subnet, thereby granting it full access to the internet.
* Configure the route table in the private subnet so that there's a default route that points to the NAT Gateway.

## Features ##

* Just like an IGW, NAT Gateway is a managed service. No management is required from the user side.

* When it comes to billing, we're charged per hour and per GB of data processed.

* One major difference between NAT Gateways and IGW is that NAT Gateways are `not region resilient`. They are configured at the subnet level and if an availability zone goes down, the NAT Gateway is lost as well.

* They use `Elastic IPs`.

* A NAT gateway supports 5 Gbps bandwidth and automatically scales up to 100 Gbps.
