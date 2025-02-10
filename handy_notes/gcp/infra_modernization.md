## Infrastructure modernization ##

The first step in moving away from an on-premises infrastructure is `colocation`, wherein a business owns a data center and other organizations rent part of that data center.
Even then, value creation only starts only after a substantial amount of capital expenditure is committed. Given that hardware is often underutilized, even in colocation model, applications and operating systems were packaged into `virtual machines` which share the same pool of computer processing, storage and network resources.

However there's still a cap to the physical capacity of existing servers and companies still have to commit to a substantial amount of capital expenditure upfront.

Cloud enables organizations to outsource their infrastructure entirely to public that offer Infrastructure as a service (IaaS).This causes a shift in IT costs from being capital expenditure heavy to operational expenditure heavy.

Opting cloud comes with the following advantages:
1. On demand self service
2. Broad network access
3. Resource pooling
4. Rapid elasticity
5. Measured service


## Compute options in Google cloud ##

There are 3 main options that can be used to modernize your infrastructure:

1. `Virtual machines (VMs)`: These are virtual computers that share the same pool of computer processing, storage and networking resources. They enable businesses to have multiple applications running at the same time on a server in a way that's efficient and manageable. The software layer that enables this is called the `hypervisor`.
The hypervisor sits on top of the physical hardware and multiple VMs are built on top of it.

2. `Containers`: Similar to VMs, they provide isolated environments to run software services and optimize resouces from one piece of hardware. However these are more efficient.
VMs recreate a full representation of the hardware, while containers only recreate or virtualize the operating system.
It thus provide a more lightweight solution with a range of benefits - 
a. They start faster
b. They use lesser memory
c. Allow devs to create predictable environments that are isolated from their obligations.

Containers can run virtually anywhere from Operating systems(Linux, Window, MacOS), VMs, Bare metal(directly on hardware) developer's machine, On-premises data center to public cloud.

`Kubernetes` is an open source cluster management system that provides automated container orchestration. It simplifies management of machines and services.

3. `Serverless computing`: It doesn't imply the absence of a server, but that resources such as compute power are automatically provided behind the scenes as and when needed. This means that businesses donot pay for compute power unless they are actually running a query or application. Businesses provide the code for whatever function they want and the public cloud provider does everything else.

Serverless computing solutions are often called function as a service.

## Google cloud compute solutions ##

### VM based ###

1. Compute engine
It's a computing and hosting service that let's you create and run VMs on google's infrastructure. They deliver scalable and high performance VMs that boot quickly, come with persistent disk storage and deliver consistent performance.
It's ideal if you need complete control over the VM infrastucture or need to run a software package that can't easily be containerized of have existing VM images to move to the cloud.

2. Google cloud VMWare engine
This is a type of software that can be run on a VM. It's a fully managed service that allows you to run the VMWare platform in Google Cloud. Here google manages the infrastucture, networking and management services.

3. Bare metal
It enables you to migrate specialized workloads to the cloud while maintaining your existing investments and architecture.
This allows access to and integration with Google Cloud services with minimal latency.

### Container based ###

4. Google Kubernetes Engine (GKE) 
GKE provides a managed environment for deploying, managing and scaling your containerized applications using Google infrastructure.
The GKE environment consists of multiple machines (Compute engine instances) grouped together to form a cluster.

### Serverless solutions ###

5. App Engine 
It's a Paas and cloud computing platform for developing and hosting web applications. It lets developers build scalable web and mobile backends in any programming language on a fully managed serverless platform, enabling them to focus on writing code without having to manage the underlying infrastructure.

6. ### Cloud Run ###
It allows developers to write applications in their favourite programming language with their favourite dependencies and deploy them in seconds while abstacting away infrastructure management by automatically scaling up and down from zero almost instantly depending on user traffic.

7. ### Cloud functions ###
It's a serverless execution environment for building and connecting cloud services. It offers a scalable pay as you go functions as services to run your code with zero server management.
It makes developers more agile as they can write and run small code snippets that respond to events.
