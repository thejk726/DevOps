## Use cases of Nginx ##

1. Web server
2. Reverse proxy
3. Load balancer
4. Cache
5. Web application firewall
6. Internal DDOS protection
7. API gateway
8. k8s IC
9. Sidecar proxy

## Configuration files ##

1. `/etc/nginx/nginx.conf` - main configuration file
2. `/etc/nginx/conf.d/*.conf` - includes (custom configurations)


## Basic commands ##

1. To check the nginx version:
```
nginx -v
```

2. To check config file syntax before reloading:
```
nginx -t
```

3. Display current configurations:
```
nginx -T
```

4. Reload nginx:
```
nginx -s reload
```
## Configuration contexts ##

* main
  |
  |---- events
  |---- http
  |      |---- server
  |      |       |
  |	 |	 |---- location
  |	 |
  |      |---- upstream
  |
  |
  |---- stream
         |
	 |---- server
	 |
	 |---- upstream

* Each Nginx configuration has one `main` context and one `http` context.

* main is the highest level directive and here we define the following:
  1. No of worker processes
  2. Location of pid file
  3. Location of log files
  4. Linux username

* `events` context is used to manage connection processing directives. Eg: no of connection per worker nodes.

* `http` context determines how nginx handles HTTP(S) connections. Eg: Address pool of backend servers. 
  Directives used in the http context are inherited by it's children contexts (Eg: server, upstream, location etc.)

* `server` context defines a virtual server that responds to a request for a domain name, ip address or a unix socket.
