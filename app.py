#!/usr/bin/env python3

import aws_cdk as cdk

from cupcake_cdk.cupcake_cdk_stack import CupcakeCdkStack


app = cdk.App()
CupcakeCdkStack(app, "cupcake-cdk")

app.synth()
