Actions.py contains some automation for functionality that can be done on the aws console.

To use Cornell resources, this link: https://confluence.cornell.edu/pages/viewpage.action?pageId=364060976 explains how to install a package called awscli login which properly lets you use Cornell SSO to run AWS commands on the command line.

The function create_compute_environment requires the names of subnets, an IAM user, and a security group ID, which seem very difficult to get without going through the setup wizard on the AWS console for AWS batch. It may be easier for that step to be done through the GUI.
