# AWS EKS (Elastic Kubernetes Service)

## What is EKS?

EKS is the AWS managed service for Kubernetes. It offers a managed control plane while allowing users to manage the data plane.

### Key Features:
- The control plane is managed by AWS and hosted in a dedicated VPC, while the user manages the data plane in their own VPC.
- Communication between control plane and data plane VPCs is enabled through Elastic Network Interfaces (ENIs).
- EKS is a **regional service** with components distributed across multiple availability zones for high availability and fault tolerance.
- EKS integrates seamlessly with a wide range of AWS services such as RDS, Load Balancers, and S3.
- EKS provides **OIDC (OpenID Connect)** endpoints, enabling mapping of users to IAM roles for secure access to the cluster.
- Logs from the cluster can be retained and monitored using **AWS CloudWatch**.

## Deployment Options
1. **AWS Management Console**
2. **CloudFormation** - AWS Infrastructure as Code (IaC) service.
3. **Terraform** - Reference: [Terraform EKS Blueprints on GitHub](https://github.com/terraform-aws-modules/terraform-aws-eks).

## Tools for EKS

### 1. **eksctl**
- A command-line utility for managing EKS clusters.
- Generates the necessary resources for cluster creation using **CloudFormation**.
- Supports:
  - Cluster lifecycle management (e.g., adding node groups, upgrading clusters).

### 2. **eksdemo**
- A tool for temporarily managing EKS clusters.
- Internally developed at AWS.
- Features:
  - Workload deployment within EKS clusters.
  - Acts as a wrapper around other command-line tools (e.g., `eksctl`).

### 3. **AWS IAM Authenticator for Kubernetes**
- A plugin for `kubectl` enabling authentication with AWS APIs to manage EKS clusters.
- Key Details:
  - The EKS API server is secured behind a load balancer requiring AWS credentials.
  - Authentication as an IAM user is necessary to call the EKS API server behind the load balancer.
