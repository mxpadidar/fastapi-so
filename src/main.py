from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from account.entrypoints.routes import router as account_router
from account.orm.mappers import start_mappers as start_account_mappers
from core import settings
from core.errors import BaseError
from core.logger import Logger

logger = Logger("main")


@asynccontextmanager
async def lifespan(_: FastAPI):
    start_account_mappers()
    yield
    logger.info("Application shutdown")


app = FastAPI(
    lifespan=lifespan,
    title=settings.APP_NAME,
    description=f"Running in {settings.APP_ENV} environment.",
)


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
    return JSONResponse(status_code=exc.status_code, content={"message": exc.message})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
