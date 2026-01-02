from fastapi import FastAPI
from app.routes import health
from app.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="GPB Mini Aula Virtual API")

app.include_router(health.router, prefix="/api")
