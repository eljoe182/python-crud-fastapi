import os
from dotenv import load_dotenv

base_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(base_dir, "../../.env"), override=True)

PORT = int(os.getenv("PORT", 3000))

DATABASE = {
    "HOST": os.getenv("DB_HOST", "localhost"),
    "PORT": os.getenv("DB_PORT", 3306),
    "USER": os.getenv("DB_USER", "root"),
    "PASSWORD": os.getenv("DB_PASSWORD", "root"),
    "DATABASE": os.getenv("DB_DATABASE", "python-crud"),
}

AWS_ENVIRONMENT = {
    "AWS_ACCESS_KEY_ID": os.getenv("AWS_ACCESS_KEY_ID", "aws-key"),
    "AWS_SECRET_ACCESS_KEY": os.getenv("AWS_SECRET_ACCESS_KEY", "aws-secret"),
    "AWS_REGION": os.getenv("AWS_REGION", "us-east-1"),
    "AWS_BUCKET_NAME": os.getenv("AWS_BUCKET_NAME", "bucket-name"),
    "AWS_URL_S3": os.getenv("AWS_URL_S3", "https://s3.amazonaws.com"),
}
