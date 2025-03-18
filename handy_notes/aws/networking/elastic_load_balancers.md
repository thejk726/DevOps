## Why load balancers? ##

Load balancers act as an intermediary between the backend servers and the client. The client would send a request to the load balancer, which would then balance the load and send it to one of the available servers in the backend pool.

## Elastic Load balacner ##

The `Elastic load balancer (ELB)` is an AWS managed load balancer service. There are three types of load balancers offered by AWS.

### 1. Classic load balancer ###

* First load balancer introduced by AWS.
* Not recommended to use.
* Limited features.

### 2. Application load balancer ###

* Supports HTTP/HTTPS/WebSockets
* Specifically for web applications.
* Operates at the application layer.
* Supports performing application specific health checks. 
* A typical flow would be - 
  1. *Client sends request with HTTP/HTTPS protocol.*
  2. *HTTP/HTTPS is terminated on ALB, ie SSL certificates reside on the ALB.*
  3. *HTTP request (unencrypted) is sent to the EC2 instance. The traffic from ALB to the instance can also be encrypted by having an SSL certificate on the instance.*

### 3. Network load balancer ###

* Load balance traffic based on TCP/UDP (layer 4).
* Meant for applications that don't use HTTP/HTTPS.
* Faster than application load balancers.
* Health checks are only basic ICMP/TCP connections.
* NLB forwards TCP connections to instances, ie. there's nothing terminated at the NLB. It acts more like a silent middle-man.

* A typical flow would be -
  1. *The client initiates a TCP or UDP session.*
  2. *The NLB forwards the connection to the instance. It acts as a proxy.*
  3. *The SSL certificate for encrypting the traffic would need to be on the EC2 instance. This ensures end to end encryption*

## Configuring the ELB ##

There are actual physical resources that get deployed when you want to utilize a load balancer. You have to select a subnet in each of the availability zones that you want to load balance to. AWS then deploys a `Load balancer node` in those subnets and then we can load balance traffic to the same or any other subnet within that availability zone.

So when a client want to send a request to one of the instances, a DNS record is created by the ELB. The DNS record forwards the requests equally to all the load balancer nodes, which then direct and load balance them across the instances.

## Cross zone load balancing ##

This feature allow LB nodes to load balance traffic across resources in different AZs.

## Load balancer deployment modes ##

### 1. Public load balancers ###

* Deployed on public subnets.
* Access by users across the public internet.

### 2. Private load balancers ###

* Deployed on private subnets.
* Deployed on private subnets.



