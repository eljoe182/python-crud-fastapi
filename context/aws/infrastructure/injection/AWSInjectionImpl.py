from shared.infrastructure.persistence.aws import AWSClient
from context.aws.infrastructure.config.AwsEnvironment import AWS_ENVIRONMENT
from context.aws.infrastructure.repository.AWSRepository import AWSRepository
from context.aws.application.AWSListFilesUseCase import AWSListFilesUseCase
from context.aws.infrastructure.controllers.AWSListFilesController import AWSListFilesController


class AWSInjectionImpl:

    def aws_list_files_impl():
        aws_client = AWSClient(AWS_ENVIRONMENT)
        aws_repository = AWSRepository(aws_client)
        use_case = AWSListFilesUseCase(aws_repository)
        return AWSListFilesController(use_case)
