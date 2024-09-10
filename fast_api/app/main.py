"""
This module initializes the FastAPI application, sets up the database connection,
and includes the user routes.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routes.user_route import user_route


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Async context manager for managing the lifespan of the FastAPI application.

    This context manager ensures that the database connection is opened before the
    application starts and closed after the application stops.

    Args:
        _app (FastAPI): The FastAPI application instance.

    Yields:
        None: Control is yielded to the application execution block.

    Raises:
        Any exceptions raised during the connection or disconnection process.

    Usage:
        This function should be used as a lifespan context manager in the FastAPI
        application to manage the database connection lifecycle.
    """
    # Conectar a la base de datos si la conexión esta cerrada
    #    if connection.is_closed():
    #        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar
        #       if not connection.is_closed():
        #           connection.close()
        print("Connection closed")


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
