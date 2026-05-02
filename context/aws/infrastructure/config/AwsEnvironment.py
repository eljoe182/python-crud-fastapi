import os

# AWS S3 / credentials (read after app.config.environment loads .env at startup).
AWS_ENVIRONMENT = {
    "AWS_ACCESS_KEY_ID": os.getenv("AWS_ACCESS_KEY_ID", "aws-key"),
    "AWS_SECRET_ACCESS_KEY": os.getenv("AWS_SECRET_ACCESS_KEY", "aws-secret"),
    "AWS_REGION": os.getenv("AWS_REGION", "us-east-1"),
    "AWS_BUCKET_NAME": os.getenv("AWS_BUCKET_NAME", "bucket-name"),
    "AWS_URL_S3": os.getenv("AWS_URL_S3", "https://s3.amazonaws.com"),
}

__all__ = ["AWS_ENVIRONMENT"]
