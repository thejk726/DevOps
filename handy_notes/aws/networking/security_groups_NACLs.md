## Stateless firewalls ##

A firewall's primary purpose is to monitor traffic and only allow traffic permitted by a set of predefined rules.
Firewall rules can be broken down into the following two categories - 

* An `inbound` rule is going to monitor incoming connections to your web server.
* An `outbound` rule is going to monitor and protect outgoing connections to the client.

Stateless firewalls must be configured to allow both inbound and outbound traffic.

## Stateful firewalls ##

* Stateful firewalls are intelligent enough to understand which request and response are part of the same connection. It's able to keep track of the TCP sessions and make out which response is meant for a particular request.

* If a request is permitted, then the response is automatically permitted.

AWS provides the following types of firewalls.

## 1. Network access control list (NACL) ##

* NACLs filter traffic entering and leaving a subnet. Every subnet will have a NACL which determine it's inbound and outbound traffic.

* NACLs `do not` filter traffic `within` a subnet.

* NACLs are `stateless` firewalls, hence rules must be set for both inbound and outbound traffic.

* Every subnet within a VPC must be associated with a network ACL.

* A NACL can be associated with multiple subnets, but a subnet must be associated with only `one` NACL at a time.

## 2. Security groups ##

* Security groups act as firewall for individual resources. Eg: EC2, LB, RDS.

* Security groups are stateful, so only the request needs to be allowed.

* We can assign multiple security groups to a single resource. The rules from all the security groups gets merged together.

* By default, security groups contain outbound rules that `allow all outbound traffic`.

### Configuring security group rules ###

1. Inbound rules - It consists of the following components:
* Name (Optional) - name for the inbound rule.
* Security group rule ID - Unique ID for that specific rule.
* IP version - IPv4 or IPv6.
* Type - request type to match, Eg: `HTTP`.
* Protocol - Protocol for the request type, Eg: `TCP`.
* Port range - Range of ports to allow traffic on.
* Source - The source to allow traffic from. 
* Description (Optional)

2. Outbound rules - It is identical to the inbound rules.

NOTE: 
Security groups, when there are no rules, block `everything`. When we add a security group rule, it allows a certain type of traffic.
All security group rules are `allow` traffic; there's no `deny` option for security groups.

NACL rules on the other hand, can `allow or deny` traffic.

### Configuring NACL rules ###

* NACL rules have an associated rule number. 
* The rules are processed in the order of these numbers. The smaller the number, the earlier the rule is processed. 

NOTE: 
NACLs do not filter traffic destined to and from the following - 
* Amazon domain name services (DNS).
* Amazon dynamic host configuration protocol (DHCP).
* Amazon EC2 instance metadata.
* Amazon ECS task metadata endpoints.
* License activation for windows instances.
* Amazon time sync service.
* Reserved IP addresses used by default VPC router.
