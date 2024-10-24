from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from account.adapters.mappers import start_mappers as start_account_mappers
from account.entrypoints.routes import router as account_router
from core import settings
from core.errors import BaseError
from core.logger import Logger

logger = Logger("main")


@asynccontextmanager
async def lifespan(_: FastAPI):
    start_account_mappers()
    yield
    logger.info("Application shutdown")


app = FastAPI(lifespan=lifespan, title=f"{settings.APP_NAME} in {settings.APP_ENV}")


app.include_router(account_router)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(BaseError)
def handle_exception(_, exc: BaseError):
    return JSONResponse(status_code=exc.code, content={"message": exc.message})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
