## What is AWS CloudWatch? ##
CloudWatch is an AWS component that enables real time monitoring of AWS resources and applications deployed on AWS infrastructure. 

## What does CloudWatch do? ##
1. Collects and tracks key metrics.
2. Collects, monitors and stores log files.
3. Creates alarms and sends notifications. 
4. Sends system events from AWS resources to AWS lambda, SNS etc.

It offers two types of monitoring: 

### Basic monitoring ( free tier )###
Resources are monitored less frequently. It polls every `5 minutes` and there's limited choice of metrics to choose from.

### Detailed monitoring ( charged ) ###
All the resources are monitored more frequently. It polls every `1 minute` and offers a wide range of metrics.

### Resources monitored by CloudWatch ###
1. EC2 instances
2. Databases in RDS
3. Data stored in S3
4. AWS Elastic load balancers
5. Other AWS resources

## Key concepts and terminologies ##
1. `metric` : Time ordered set of data points that are published to CloudWatch. Think of it as a variable to monitor and the datapoints represents the value of that variable over time.

2. `dimension` : It's a name/value pair that uniquely identifies a metric. They can be considered as categories of characteristics that describe a metric. We can assign upto 10 dimensions to a metric.

3. `statistics` : Metric data aggregations over specified periods of time. Aggregations are made using the namespace, metric name, dimensions within the time period you specify.

4. `Alarm` : Can be used to automatically initiate actions on your behalf. It watches a single metric over a specified time period and performs one or more specified actions.

## How CloudWatch works? ##

CloudWatch has complete visibility into AWS resources and applications. 

`Collect` : It collects metrics and logs from from all the resources and applications.
`Monitor` : Enables visualization of these metrics on CloudWatch dashboard.
`Act` : If any operational changes are detected, it provides for automated responses to these changes.
`Analyze` : It also provides for real time analysis using CloudWatch metric math which integrates multiple CloudWatch metrics and creates a new time series.

## CloudWatch events ##

An `event` indicates a change in AWS environment. AWS resources generate an event when a resource changes. Amazon CloudWatch events is a part of CloudWatch that generates a near real time stream of system events that allow you to monitor and respond to changes in your AWS resources by means of rules that route events to one or more targets.

## Rules ##

`Rules` evaluate an incoming event to determine if a threshold or out of bounds scenario exists. If yes, then the event is routed to a target.

## Targets ##

A target processes events that are passed from a rule. A rule may invoke multiple targets. Targets may include EC2 instances, Lambda functions etc. 


## CloudWatch logs ##

Logs are detailed record of events that occur in the AWS environment. It's used to monitor, store and access log files from AWS resources.

### Log event ###
It is the record of activity by resources or application being monitored.

### Log stream ###
Sequence of log events that share the same source.

### Log groups ###
These are groups of log streams that share same monitoring and access control settings. Each log stream must belong to a log group.
