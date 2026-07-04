from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.device import DeviceCreate, DeviceResponse , DeviceUpdate
from app.crud.device import create_device

from fastapi import HTTPException
from app.crud.device import (
    create_device,
    get_devices,
    get_device,
    delete_device,
)

from app.services.device_service import update_device_service

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

@router.get("/", response_model=list[DeviceResponse])
def read_devices(db: Session = Depends(get_db)):
    return get_devices(db)

@router.get("/{device_id}", response_model=DeviceResponse)
def read_device(device_id: int, db: Session = Depends(get_db)):
    device = get_device(db, device_id)

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    return device


@router.delete("/{device_id}")
def remove_device(device_id: int, db: Session = Depends(get_db)):
    device = delete_device(db, device_id)

    if not device:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    return {
        "message": "Device deleted successfully"
    }

@router.put("/{device_id}", response_model=DeviceResponse)
def update_device(
    device_id: int,
    device: DeviceUpdate,
    db: Session = Depends(get_db)
):
    updated_device = update_device_service(db, device_id, device)

    if updated_device is None:
        raise HTTPException(
            status_code=404,
            detail="Device not found"
        )

    return updated_device