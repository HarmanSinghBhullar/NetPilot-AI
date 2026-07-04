from sqlalchemy.orm import Session
from app.models.device import Device
from app.schemas.device import DeviceCreate
from app.schemas.device import DeviceUpdate

def create_device(db: Session, device: DeviceCreate):
    db_device = Device(**device.model_dump())
    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device


def get_devices(db: Session):
    return db.query(Device).all()


def get_device(db: Session, device_id: int):
    return db.query(Device).filter(Device.id == device_id).first()


def delete_device(db: Session, device_id: int):
    device = db.query(Device).filter(Device.id == device_id).first()

    if device:
        db.delete(device)
        db.commit()

    return device

def update_device(
    db: Session,
    device_id: int,
    updated_device: DeviceUpdate
):
    device = db.query(Device).filter(Device.id == device_id).first()

    if device is None:
        return None

    # Get all fields from the request
    update_data = updated_device.model_dump()

    # Update each field dynamically
    for key, value in update_data.items():
        setattr(device, key, value)

    db.commit()
    db.refresh(device)

    return device