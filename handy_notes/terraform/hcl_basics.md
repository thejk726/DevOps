## HCL syntax ##

An HCL file consists of `blocks` and `arguments`. 
* A block is enclosed in curly braces and it consists of arguments in key-value format representing the configuration data.
* A block in terraform contains information about the infrastructure platform and a set of resources we want to create within that platform.

* The basic syntax of a minimal HCL is as follows:
  <block name> "<provider>\_<resource>" "<resource name> {
  <arguments> (key=value)
  }


