from context.aws.application.AWSListFilesUseCase import AWSListFilesUseCase


class AWSListFilesController:
    def __init__(self, use_case: AWSListFilesUseCase):
        self._use_case = use_case

    def run(self, bucket_name: str):
        return self._use_case.execute(bucket_name)
