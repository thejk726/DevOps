## Routing in VPCs ##

Every VPC has a VPC router and this router has an interface in every subnet of the VPC which can be reachable from the network + 1 address of each subnet.
Eg: If our subnet is 192.168.1.0/24, the router's interface in the subnet will be 192.168.1.1.

The purpose of the router is to route traffic between the subnets as well as in and out of the VPC.

Just like a normal router in a data center, the `route tables` of the router can be configured to determine where the network traffic will get sent.

## Route table ##

* A route table is a set of rules that the router uses to forward traffic.

* Each rule in the route table is called a `route`.

* A router will check any packet leaving the subnet and will check only the `destination IP` of the packet. It will then find a matching route by checking the destination column. 

* In case of overlap between two routes, AWS is going to pick the route with the larger prefix length.
  Eg: If there are two routes - 10.16.0.0/16 and 10.16.1.0/24, the latter is going to be selected.

* All route tables have only one route by default, which is the `local` route. This route will match all the destination routes from the VPC as the destination IP is the VPC CIDR. So any traffic originating within the VPC bound for any other device in the same VPC will match the local route here.

* Every subnet is associated with one route table. When we configure a subnet, we can specify which route table it's associated with.

* When a new subnet is created, a default route table is automatically created for it. The subnet will by default be associated with this route table until you point them to a different one.

* `Multiple` subnets can be associated with a `single` route table, but a subnet can only be associated with `one` route table in total.

## Creating a route table ##

1. Under the VPC go to the route tables section.
2. Select `Create route table`.
3. Specify route table name and the assocaited VPC.
4. Select `Create route table` to finish.
5. Associate subnets with the route table.
6. Add routes as desired by clicking on `Edit routes`.

* 


