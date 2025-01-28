## What are probes? ###


### NOTE ###
Probes are defined at the `container` level, not at the `pod` level.

## Probing mechanisms ##
### 1. Exec ###
Here a command is executed inside a container. If the command executes with an exit code of `0`, the container is assumed to be healthy and if it executes with an exit code of `1`, it's assumed to be unhealthy.

#### Example ####
```
exec:
  command:
    - mongo
    - --eval
    - "db.adminCommand('ping')"
```

### 2. Network calls ###
### 2.1 HTTP ###
In this method, we ask kubernetes to make an HTTP call to an endpoint within the container. If the container issues an HTTP response in the 200 to 399 range, the container is assumed to be healthy and unhealthy otherwise.

#### Example ####
```
httpGet:
  path: /healthz
  port: 8080
```
### 2.2 TCP ###
In this method, we try to open a port on the container. The probe is considered to be successful if the specific container port accepts traffic and is considered a failure otherwise.

#### Example ####
```
tcpSocket:
  port: 8080
```

## Types of probes ##
There are three types of probes defined in kubernetes. They are - 

### Liveness probe ###

Liveness probes allow us to instruct kubernetes on how to detect whether a pod is live or not.
If a liveness probe returns `exit code =1`, which indicates failure, kubernetes assumes the pod to be unhealthy and the kubelet restarts the pod. 
It ensures that we always have healthy pods available.

Eg:
```
livenessProbe:
  exec:
    command: 
      - mongo
      - --eval
      - "db.adminCommand('ping')"
  initialDelaySeconds: 1
  periodSeconds: 10
  timeoutSeconds: 5
  successThreshold: 1
  failureThreshold: 2

```

Let's go over the directives in the exec section.

`initialDelaySeconds` : Delay to run the probe initially. The value `1` indicates that the probe will wait for one second after the container is up for the first check.

`periodSeconds` : Specifies how frequently the probe should execute after the initial delay. Here, the value `10` indicates that the probe would execute every 10 seconds after the initial delay.

`timeoutSeconds` : Timeout period to mark as failure. Here the value `5` indicates that if the probe doesn't succeed within 5 seconds it's assumed to have failed.

`success/failureThreshold` : Specifies how many times to retry in case of failures.  

### Readiness probe ###

This probe identifies when a container can handle external traffic received from a service. In case of failure, kubernetes removes the pod's IP addresses from the endpoints of all services it belong to. Once the readiness probe succeeds, it's added back to the service, ready to serve traffic.

Eg:
```
readinessProbe:
  exec:
    command: 
      - mongo
      - --eval
      - "db.adminCommand('ping')"
  initialDelaySeconds: 1
  periodSeconds: 10
  timeoutSeconds: 5
  successThreshold: 1
  failureThreshold: 2

```

### Startup probe ###
This probe delays the execution of liveness and readiness probes until the container indicates it's able to handle them i.e, liveness and readiness probes are executed only if the startup probe succeeds. Upon failure, the container is killed and follows the restart policy.

It should be used when the application within our container takes a significant amount of time to reach it's normal operating state. This is done so that the liveness and readiness probes don't fail.

Eg:
```
startupProbe:
  exec:
    command: 
      - mongo
      - --eval
      - "db.adminCommand('ping')"
  initialDelaySeconds: 1
  periodSeconds: 10
  timeoutSeconds: 5
  successThreshold: 1
  failureThreshold: 2

```

## Best practises ##

1. The frequency for probe execution should be ideal. Too high a frequency can lead to wastage of compute resources. Too less and the container may be in an unhealthy state for too long.

2. Probes should be as lightweight as possible. To ensure the probes are executed quickly, avoid using expensive operations within the probes. 

3. Define the correct restart policy.

4. Use probes only when needed.