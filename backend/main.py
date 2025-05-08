from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.routes.api import api_router
from core.config import settings
from core.logger import InterceptHandler, format_record

from loguru import logger
import logging
import sys
import uvicorn
def create_app() -> FastAPI:
    """
    Create FastAPI application instance.
    """
    app = FastAPI(title=settings.PROJECT_NAME)
    if settings.SERVER == False:
        app.debug = True
    if settings.SERVER == True:
        app.debug = False
        app.redoc_url = None
        app.docs_url = None

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.all_cors_origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["Access-Control-Allow-Origin, Content-Type", "Authorization"],
        expose_headers=["Content-Disposition"],
    )

    return app
app = create_app()
# app = FastAPI(title=settings.PROJECT_NAME)
# if settings.SERVER == False:
#     app.debug = True
# if settings.SERVER == True:
#     app.debug = False
#     app.redoc_url = None
#     app.docs_url = None

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=settings.all_cors_origins,
#     allow_credentials=True,
#     allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
#     allow_headers=["Access-Control-Allow-Origin, Content-Type", "Authorization"],
#     expose_headers=["Content-Disposition"],
# )

app.include_router(api_router)

loggers = (
    logging.getLogger(name)
    for name in logging.root.manager.loggerDict
    if name.startswith("uvicorn.")
)
for uvicorn_logger in loggers:
    uvicorn_logger.handlers = []

logging.getLogger("uvicorn").handlers = [InterceptHandler()]

logger.configure(handlers=[{"sink": sys.stdout, "level": logging.INFO, "format": format_record}])
if settings.SERVER == True:
    logger.add(settings.PROJECT_ROOT + "/logs/api.log", rotation="1 day")

# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=9000)
