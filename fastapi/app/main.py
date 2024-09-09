from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from database import database as connection
from routes.user_route import user_route


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a la base de datos si la conexión esta cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar
        if not connection.is_closed():
            connection.close()


# app instance
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def root():
    """
    Root endpoint that redirects to the API documentation.

    Returns:
        RedirectResponse: A response object that redirects the client to the "/docs" URL.
    """
    return RedirectResponse(url="/docs")


# -------- Usuario --------
app.include_router(user_route, prefix="/api/users", tags=["Users"])
