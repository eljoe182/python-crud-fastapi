from fastapi import APIRouter
from app.injection_dependencies.AWSInjectionImpl import AWSInjectionImpl


router = APIRouter(prefix="/aws", tags=["AWS"])


@router.get("/list-files/{bucket_name}")
def list_files(bucket_name: str):
    return AWSInjectionImpl.aws_list_files_impl().run(bucket_name)
