from constructs import Construct
from aws_cdk import (
    aws_cloudfront_origins,
    Stack,
    aws_iam as iam,
    aws_s3 as s3,
    aws_cloudfront as cf
)


class CupcakeCdkStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self, 
            "cupcake_cms",
            block_public_access=s3.BlockPublicAccess.BLOCK_ALL
        )
        
        oai = cf.OriginAccessIdentity(self, "OAI", comment="Connects CF with S3")
        bucket.grant_read(oai)
        
        distribution = cf.Distribution(
            self,
            "CDN",
            minimum_protocol_version=cf.SecurityPolicyProtocol.TLS_V1_2_2018,
            default_behavior=cf.BehaviorOptions(
                allowed_methods=cf.AllowedMethods.ALLOW_ALL,
                origin=aws_cloudfront_origins.S3Origin(
                    bucket=bucket,
                    origin_access_identity=oai,
                    origin_path="/",
                ),
                viewer_protocol_policy=cf.ViewerProtocolPolicy.REDIRECT_TO_HTTPS,
            )
        )
