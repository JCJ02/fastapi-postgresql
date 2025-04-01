from fastapi import FastAPI, HTTPException, Depends
from api.utilities.database_connection import engine, SessionLocal, get_database
from api.models.user_model import Base

app = FastAPI(
    title = "FastAPI with PostgreSQL",
    description = "API Template"
)

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)