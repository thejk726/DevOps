## Subnets ##

* Subnets are groups of IP addresses within your VPC. A subnet resides within a single availability zone. 

* Subnets can be made `public` or `private` to allow external access to resources within them. So anything that doesn't need to be externally accessible, can be deployed to a private subnet and vice-versa.

* A subnet can be made public or private using gateways like `Internet gateways` or `NAT gateways`.

* Subnets within a VPC must be within the CIDR range.

* A subnet block size must be between `/16` and `/28`.

* The first 4 IP addresses of a subnet are reserved and cannot be used. 
Eg: Consider a network with CIDR block `192.168.0.0/16. The address `192.168.10.0/24` would be a valid subnet. 
In this subnet, The followind IP addresses would be reserved and cannot be used -
1. `192.168.10.0` - network address
2. `192.168.10.1 - 192.168.10.3` - for AWS
    a. `192.168.10.1` - VPC router
    b. `192.168.10.2` - DNS 
    c. `192.168.10.3` - for future use

3. `192.168.10.255` - broadcast address

* Subnets cannot overlap with other subnets in the `same` VPC.
  Eg: The following IP addresses would not be possible for two subnets in a VPC -
      Subnet A : `10.16.0.0/24`
      Subnet B : `10.16.0.128/25`

* We can also configure a subnet to use an optional IPv6/56 CIDR block or to only use an IPv6 CIDR block.

* Subnets can communicate with other subnets in the VPC without any additional configurations. 

* We can also auto-assign public IPv4/IPv6 addresses in addition to the private address.

## Creating a subnet ##

1. Choose a VPC
2. Under `Subnets` section, choose `Create subnet`.
3. Name your subnet.
4. Choose an availability zone.
5. Specify the IPv4 CIDR.
6. Specify the IPv6 CIDR (Optional).
7. Click `Create subnet` to finish.

### NOTE ###
To deploy a server into a particular availability zone, we must specify the corresponding subnet.

 
