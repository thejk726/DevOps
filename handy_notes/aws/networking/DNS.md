## DNS (VPC) ##

* AWS provides DNS servers for domain name resolution. 
* These servers can be accessed by sending a DNS request to the IP `169.254.169.253`, which all your resources will have access to, or by sending a DNS query to the 2nd IP address of the VPC CIDR block.
  Eg: If there's a VPC with CIDR 10.10.0.0/16, the DNS server can be reached at 10.10.0.2
* By default, only `private` IPs get a DNS entry and public ones don't. If you want public IP addresses to also get a domain name, the `enableDnsHostnames` option when creating the VPC. Then to enable DNS resolution in the VPC so that we can utilize the AWS DNS servers, we have to make sure that we enable the `enableDnsSupport` knob.
   a. `enableDnsHostnames` - Determines whether the VPC supports assigning public DNS hostnames to instances with public IP        addresses.
   b. `enableDnsResolution` - Determines whether the VPC supports DNS resolution through the amazon provided DNS server.

 

