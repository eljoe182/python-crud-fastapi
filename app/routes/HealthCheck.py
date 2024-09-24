from shared.infrastructure.observability.logger import LoggerObserver
from fastapi import APIRouter

router = APIRouter(prefix="/health-check", tags=["Health Check"])
logging = LoggerObserver(__name__)


@router.get("/")
def health_check():
    logging.info("Health check")
    return {"status": "ok"}
