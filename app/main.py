from fastapi import FastAPI

from app.core.database import engine

from app.models import device as device_model

from app.routers import device as device_router

device_model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="NetPilot AI",
    version="1.0"
)

app.include_router(device_router.router)


@app.get("/")
def root():
    return {
        "Project": "NetPilot AI",
        "Status": "Running"
    }

