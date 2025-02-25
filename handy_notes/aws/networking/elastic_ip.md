## Elastic IPs ##

The public IPs assigned to EC2 instances are epehemeral. To save the trouble of constantly keeping track of IP addresses, elastic IPs can be used. 

* Elastic IP addresses are static IPv4 addresses that can be allocated to our account. Once allocated, it's resreved for your account.
* We can then associate this IP address to a server, which will then always have this IP address even if the instance is rebooted or get moved to another physical host.
* We can assign security group to an elastic IP, so it's going to be like a fixed network configuration to that specific interface.
* We can dissociate an elastic IP from an instance and associate it with another one and have the traffic be redirected to the new target. This can be useful when maintainance work is required to be done on an instance.
* In terms of pricing, we can have an elastic IP associated with a running instance at no charge, but in case of additional elastic IPs, the additional IPs are charged per hour. Also if we reserve an elastic IP, but we don't associate it with anything, it's going to incur a small hourly charge as well.
* They are specific to a region and can only be associated with EC2 instances within that region.

## Allocating an elastic IP ##

* In the EC2 dashboad, go to `Elastic IPs`.
* Select `Allocate elastic IP address`. 
* Specify the network border group.
* Select the IPv4 address pool.
* Click `Allocate` to finish.

##  Associating the elastic IP with an instance ##

* Go to `Actions` >> `Associate elastic IP address`.
* Choose instance/network interface depending on the particular use case.
* Choose the instance/network interface.
* In case of multiple private IP addresses, specify which IP address to associate it with.
* Click on `associate` to finish.

## Releasing an elastic IP ##

* First disassociate the elastic IP by selecting `Actions` >> `Disassociate elastic IP address`.
* Go to `Actions` >> `Release elastic IP address`.
