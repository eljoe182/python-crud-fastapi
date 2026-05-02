from botocore.config import Config


class AWSConfig:
    def __init__(self, settings: dict):
        self._key = settings.get("AWS_ACCESS_KEY_ID")
        self._secret = settings.get("AWS_SECRET_ACCESS_KEY")
        self._region = settings.get("AWS_REGION")
        self._bucket = settings.get("AWS_BUCKET_NAME")
        self._endpoint_url = settings.get("AWS_URL_S3")

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
