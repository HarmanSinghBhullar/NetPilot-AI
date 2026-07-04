from pydantic import BaseModel

class DeviceCreate(BaseModel):
    hostname: str
    ip_address: str
    device_type: str
    location: str | None = None


class DeviceResponse(DeviceCreate):
    id: int

    class Config:
        from_attributes = True

class DeviceUpdate(BaseModel):
    hostname: str
    ip_address: str
    device_type: str
    location: str | None = None