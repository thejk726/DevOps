## HCL syntax ##

An HCL file consists of `blocks` and `arguments`. 
* A block is enclosed in curly braces and it consists of arguments in key-value format representing the configuration data.
* A block in terraform contains information about the infrastructure platform and a set of resources we want to create within that platform.

* The basic syntax of a minimal HCL is as follows:
  <block name> "<provider>\_<resource>" "<resource name> {
  <arguments> (key=value)
  }

## Example ##

1. Here's a simple terraform script to create a file using the resource type `local_file`.

```
resource "local_file" "example_file" {
filename="sample.txt"
content="Sample content"
}
```

* Here, `local` is the provider and `file` is the resource.
* `example_file` is the resource name.
* The 2 arguments `filename` and `content` defines the complete absoulute path of the file and the file content respectively.

* Once the file is created, we run the following command to initialize the terraform directory

```
terrafrom init
```

This checks the script file and downloads all the required plugins for the provider.

* To view the effect of running the script, we run the folowing command - 

```
terraform plan
```

This provides a preview of the state of the system once the changes are applied.

* To apply the changes, we run the following command - 

```
terraform apply
```

This applies the script and brings the system to the desired state, ie the file is created.

* To update the state of the system, the terraform script needs to be updated and applied again. For instance, to change the permission of the file from the default `0777` to `0700`, we update the script as follows -

```
resource "local_file" "example_file" {
filename="sample.txt"
content="Sample content"
file_permission="0700"
}
```

and then apply the updated script as before to apply the changes. This will completely replace the file, ie remove the existing file and create a new file with the specified changes.

* To destroy the resources created, we use the following command - 
```
terraform destroy
```




