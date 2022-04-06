"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

caller_id = aws.get_caller_identity()
