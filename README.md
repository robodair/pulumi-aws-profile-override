# Reproduce error configuring Terraform AWS Provider

The `Pulumi.dev.yaml` stack config contains `aws:profile: profile-that-doesnt-exist`.

We want to leave this configuration there, but instead use credentials explicitly specified with `AWS_SECRET_ACCESS_KEY` and `AWS_ACCESS_KEY_ID`. This works as expected with `pulumi-aws<5.0.0` but has stopped with pulumi-aws>=5.0.0. Though the behavior has changed again in 5.1.0.

pulumi-aws >= 5.0.0:

```
$ AWS_SECRET_ACCESS_KEY=bar AWS_ACCESS_KEY_ID=foo pulumi preview
...
Exception: invoke of aws:index/getCallerIdentity:getCallerIdentity failed: invocation of aws:index/getCallerIdentity:getCallerIdentity returned an error: 1 error occurred:
    	* error configuring Terraform AWS Provider: failed to get shared config profile, profile-that-doesnt-exist
    error: an unhandled error occurred: Program exited with non-zero exit code: 1
...
```

pulumi-aws==5.0.0:

```
$ AWS_SECRET_ACCESS_KEY=bar AWS_ACCESS_KEY_ID=foo pulumi preview
...
Exception: invoke of aws:index/getCallerIdentity:getCallerIdentity failed: invocation of aws:index/getCallerIdentity:getCallerIdentity returned an error: 1 error occurred:
    	* error configuring Terraform AWS Provider: no valid credential sources for Terraform AWS Provider found.

Please see https://registry.terraform.io/providers/hashicorp/aws
for more information about providing credentials.

Error: no EC2 IMDS role found, operation error ec2imds: GetMetadata, access disabled to EC2 IMDS via client option, or "AWS_EC2_METADATA_DISABLED" environment variable
...
```

If we downgrade to pulumi-aws<5.0.0 the preview is successful.
