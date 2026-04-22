from fastapi import FastAPI

from app.api.routes_auth import router as auth_router
from app.db.base import Base
from app.db.session import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Auth API FastAPI JWT",
    version="1.0.0",
    description="Authentication API with JWT and role-based access control.",
)

app.include_router(auth_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Auth API is running"}
