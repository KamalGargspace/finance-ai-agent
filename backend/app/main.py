from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router

from app.database import engine
from app.models.invoice import Invoice
from app.models.audit_log import AuditLog
from app.database import Base
from contextlib import asynccontextmanager

from app.scheduler.scheduler import (
    scheduler
)

# Create database tables
Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(app: FastAPI):

    print("Starting scheduler...")

    scheduler.start()

    yield

    print("Stopping scheduler...")

    scheduler.shutdown()


app = FastAPI(

    title="Finance Credit Follow-Up Agent",

    version="1.0.0",

    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)

@app.get("/")
def home():
    return {
        "message": "Finance Credit Agent Backend Running"
    }