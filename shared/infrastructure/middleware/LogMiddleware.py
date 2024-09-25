import time
from fastapi import Request
from shared.infrastructure.observability.logger import LoggerObserver

logger = LoggerObserver('log_middleware')

async def LogMiddleware(request: Request, call_next):
    logger.info(f"Request: {request.url}")
    logger.info(f"Method: {request.method}")
    logger.info(f"Headers: {request.headers}")

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    logger.info(f"Process time: {process_time}")

    return response
