from sqlalchemy.orm import Session
from app.schemas.device import DeviceUpdate
from app.crud.device import update_device


def update_device_service(
    db: Session,
    device_id: int,
    device: DeviceUpdate
):
    return update_device(db, device_id, device)