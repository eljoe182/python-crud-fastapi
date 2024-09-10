from shared.infrastructure.persistence.aws import AWSClient
from context.aws.infrastructure.repository.AWSRepository import AWSRepository
from context.aws.application.AWSListFilesUseCase import AWSListFilesUseCase
from app.controllers.aws.AWSListFilesController import AWSListFilesController


class AWSInjectionImpl:

    def aws_list_files_impl():
        aws_client = AWSClient()
        aws_repository = AWSRepository(aws_client)
        use_case = AWSListFilesUseCase(aws_repository)
        return AWSListFilesController(use_case)
