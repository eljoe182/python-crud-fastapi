from shared.infrastructure.persistence.aws import AWSClient


class AWSRepository:
    def __init__(self, client: AWSClient):
        self._clientS3 = client.get_client_s3()

    def list_files(self, bucket_name: str):
        response = self._clientS3.list_objects_v2(Bucket=bucket_name)
        return response.get("Contents", [])
