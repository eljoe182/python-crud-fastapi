import time
from fastapi import Request


async def MetricsMiddleware(request: Request, call_next):
    start_time = time.time()
    response = call_next(request)
    process_time = time.time() - start_time
    request.headers["X-Process-Time"] = str(process_time)
    return response
