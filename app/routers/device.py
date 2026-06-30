from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.device import DeviceCreate, DeviceResponse
from app.crud.device import create_device

router = APIRouter(
    prefix="/devices",
    tags=["Devices"]
)


@router.post("/", response_model=DeviceResponse)
def add_device(
    device: DeviceCreate,
    db: Session = Depends(get_db)
):
    return create_device(db, device)