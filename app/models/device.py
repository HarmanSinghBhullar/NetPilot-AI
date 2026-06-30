from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import DateTime

from datetime import datetime

from app.core.database import Base


class Device(Base):

    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, index=True)

    hostname = Column(String(50), nullable=False)

    ip_address = Column(String(50), nullable=False)

    device_type = Column(String(50), nullable=False)

    location = Column(String(100))

    created_at = Column(DateTime, default=datetime.utcnow)