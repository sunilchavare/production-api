from fastapi import FastAPI
from app.db.database import engine, Base
from app.api.routes.users import router as users_router
from app.api.routes.auth import router as auth_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Production API")

app.include_router(auth_router, prefix="/api/v1", tags=["auth"])

app.include_router(users_router, prefix="/api/v1", tags=["users"])
