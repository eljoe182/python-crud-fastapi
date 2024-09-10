import boto3.session

from .Config import AWSConfig


class AWSClient:
    def __init__(self):
        self._config = AWSConfig()

    def get_client_s3(self):
        key, secret = self._config.get_credentials_s3()
        region = self._config.get_region_s3()
        configS3 = self._config.get_config_bucket_s3()

        session = boto3.Session(
            aws_access_key_id=key,
            aws_secret_access_key=secret,
            region_name=region,
        )

        return session.client(
            "s3",
            config=configS3,
            endpoint_url=self._config.get_endpoint_url_s3(),
        )
