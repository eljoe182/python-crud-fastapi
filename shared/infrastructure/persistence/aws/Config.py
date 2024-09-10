from botocore.config import Config
from app.config.environment import AWS_ENVIRONMENT


class AWSConfig:
    def __init__(self):
        self._key = AWS_ENVIRONMENT.get("AWS_ACCESS_KEY_ID")
        self._secret = AWS_ENVIRONMENT.get("AWS_SECRET_ACCESS_KEY")
        self._region = AWS_ENVIRONMENT.get("AWS_REGION")
        self._bucket = AWS_ENVIRONMENT.get("AWS_BUCKET_NAME")
        self._endpoint_url = AWS_ENVIRONMENT.get("AWS_URL_S3")

    def get_bucket_s3(self):
        return self._bucket

    def get_region_s3(self):
        return self._region

    def get_endpoint_url_s3(self):
        return self._endpoint_url

    def get_config_bucket_s3(self):
        return Config(
            signature_version="s3v4",
            region_name=self._region,
            retries={
                "max_attempts": 10,
                "mode": "standard",
            },
        )

    def get_credentials_s3(self):
        return self._key, self._secret
