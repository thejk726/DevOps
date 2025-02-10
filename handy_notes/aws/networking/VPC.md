## What is a VPC ##
It's a secure, isolated network segment hosted within AWS. It allows us to isolate resources from other resources in the cloud ie. it acts as a network boundary.
Any communication between VPCs or a VPC and the internet has to be explicitly allowed.

It grants the customer full control of networking in the cloud, which enables:
1. Subnetting (IP addresses)
2. Routing (Route tables)
3. Firewalls (NACLS and security groups)
4. Gateways

### NOTE ###
A VPC is specific to a single region. You have to specify the region where you want the VPC to be created.

Every VPC has a range of IP addresses assigned to it called the `CIDR block`. It defines the IP addressed that the resources in the VPC can use. A CIDR block size can be anywhere from a /16 to a /28

There's provision to optionally enable a `secondary IPv4 CIDR block` or an `IPv6 /56 CIDR block`. We can have upto `5` IPv6 CIDR blocks for our network, but this limit is adjustable.

## Types of VPC ##

### Default VPC ###

These are configured by AWS on your behalf. Any time you create an AWS account, AWS is going to configure a default VPC in every single region that you have access to. They'll have a certain level of default configuration.
They'll automatically allow internet connectivity for your resources.

The default VPCs comes with the following out of the box configurations:
1. One default VPC per region
2. Every single default VPC will use a /16 IPv4 CIDR block (65,536 addresses) and it's going to be 172.31.0.0/16 for all AWS accounts
3. For every availability zone in the region your default VPC is configured in will get one /20 default subnet
4. An internet gateway is going to be attached to the VPC
5. There will be a default route (0.0.0.0/0) which points all traffic to the internet gateway.
   This grants internet access to all the resources in the default VPC, ie. resources in these default subnets will be accessible from the internet
6. There will be a default security group assigned to your resources which by default allow outbound traffic
7. There will also be a default Network Access Control List to secure the subnets and the VPC overall which by default allows both inbound and outbound traffic

### Custom VPC ###

These are built by you with custom configurations.

### Creating a custom VPC ###

1. Select the region to create the VPC.
2. Go to VPC --> your VPC's.
3. Click `Create VPC`.
4. Select either `VPC only` or `VPC and more`
5. If selecting `CIDR mannual input`, specify the desired IP address range (IPv4 CIDR).
6. Opt for an IPv6 CIDR block if needed (optional).
7. Select tenancy for the VPC.
8. Specify the tags for the VPC.
9. Click create VPC.
