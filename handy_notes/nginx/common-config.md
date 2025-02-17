## Common configurations ##

### 1. /etc/nginx/nginx.conf ###

There are 4 notable items in this file -
a. `user` - The user which runs the nginx process
b. `worker_processes` - Defines the number of worker processes that the nginx server will have
c. `error_log` - It may consist of the following 2 parts - 
    1. The path to the log files (access.log, error.log)
    2. The log level
    Eg: /var/log/nginx/access.log warn, where warn is the log level and messages from all severity levels above the one specified are logged.
d. `pid` - It defines the location of the pid file of the nginx process

These 4 are part of the main context, ie they are not part of any particular server block, but are configurations for the nginx server itself.

### 2. /etc/nginx/conf.d/default.conf ###

This file defines the default configuration for the nginx server.

## Overview of a typical configuration file ##

 ### The server block ###
This is a configuration section that defines how nginx should handle requests for a specific domain or IP address.

#### Key Purpose of a Server Block ####

1. Host Multiple Websites on the Same Server

2. You can configure different domain names (e.g., site1.com, site2.com) and direct traffic to the correct location.
Redirect Traffic Based on Domains or Subdomains
Example: Requests to example.com can go to one directory, while blog.example.com goes to another.
Apply Different Settings for Each Site

3. Logging, SSL, caching, reverse proxy rules, and more can be customized per site.

It contains the following directives:
a. `listen` - specifies the port to listen on. Eg: listen 80
b. `server_name` - defines the domains that this block should handle. Eg: server_name example.com www.example.com
c. `location <path>` - defines how the requests to a particular path should be handled. This specifies the context for redirection when the request for a particular path is received.
Eg:

```
location / {
root /usr/share/nginx/html
index index.html index.htm
}
```

The above location block sets the context when the request for the root path (/) is received. 
`root` directive defines the directory to look for contents to serve.
`index` directive defines the files to serve in the root directory.

d. `error_page <error_code> <path_to_custom_page>` - This directive allows you to customize error messages that users see when something goes wrong on your website. Instead of the default nginx error message, you can show your own custom error page.

```
server {
    listen 80;
    server_name example.com;

    root /var/www/example;

    # Custom 404 error page
    error_page 404 /custom_404.html;

    location / {
        try_files $uri $uri/ =404;
    }

    location = /custom_404.html {
        
        internal;  # Prevent direct access to the error page
    }
}
```

Here on a 404 error, the request is redirected to a custom 404 page. 
The `internal` directive prevents users from accessing /custom_404.html directly.


