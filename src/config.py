from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    PATH_TO_LOCAL_FILES: str

    CELERY_BROKER_URL: str = "redis://localhost:6379"
    CELERY_RESULT_BACKEND: str = "redis://localhost:6379"
    CELERY_IMPORTS: tuple = ("src.services.files",)

    USE_S3_STORAGE: bool
    S3_BUCKET: str
    S3_KMS_KEY_ID: str

    @property
    def STORAGE_OPTIONS(self):
        if self.USE_S3_STORAGE:
            return {
                "s3_additional_kwargs": {
                    "ServerSideEncryption": "aws:kms",
                    "SSEKMSKeyId": self.S3_KMS_KEY_ID,
                }
            }
        return None

    @property
    def STORAGE_PATH(self):
        if self.USE_S3_STORAGE:
            return f"s3://{self.S3_BUCKET}"
        return self.PATH_TO_LOCAL_FILES

    class Config:
        env_file = ".env"


@lru_cache()
def get_settings():
    return Settings()
