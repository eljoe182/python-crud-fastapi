from context.aws.infrastructure.repository.AWSRepository import AWSRepository


class AWSListFilesUseCase:
    def __init__(self, repository: AWSRepository):
        self._repository = repository

    def execute(self, bucket_name: str):
        return self._repository.list_files(bucket_name)
