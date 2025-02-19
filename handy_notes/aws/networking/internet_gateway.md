## Internet Gateway ##

By default, a subnet will be `private`, ie devices within the subnet cannot talk to the internet and vice versa. 
To make subnets public, an `internet gateway` is to be used.

* Internet gateways are attached to VPCs and are `region resilient`. This means they cover all the availability zones within a region.

* If a VPC does not have an internet gateway attached to it, all of it's subnets will be considered private.

* A VPC can have upto `one` internet gateway attached to it and an internet gateway can be attached to only `one` VPC at a time.

* There are the following steps associated in making a subnet public - 
  1. Create an internet gateway.
  2. Attach the IGW to the VPC.
  3. Create a custom route table.
  4. Configure default route ( pointing to the IGW ). 
  5. Associate the desired subnet with the route table.

* By default, when a resource is deployed onto a public subnet, it's only going to get a private IP. 

* A resource deployed on a subnet won't know anything about the public IP associated with it.

## Create an Internet Gateway ##

1. Go to VPC >> `Internet gateways`.
2. Select `Create internet gateway`. 
3. Specify IGW name.
4. Click `Create internet gateway` to finish.
5. Go to `Actions` >> `Attach to VPC`.
6. Select the VPC.

## Configure internet access ##

The route table has to be configured so that the router knows to send traffic meant for the internet towards the IGW.

* Add default route (0.0.0.0/0) to the route table (default or new) and point it to the internet gateway.
