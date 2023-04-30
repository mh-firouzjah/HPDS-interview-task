from datetime import datetime

from pydantic import BaseModel as PydanticBaseModel
from sqlalchemy import Column, DateTime, Integer

from database import Base


def custom_datetime_format(dt: datetime):
    return dt.strftime("%Y-%m-%d %H:%M")


class PydanticMemInfo(PydanticBaseModel):
    id: int
    created: datetime
    total: int
    used: int
    free: int

    class Config:
        orm_mode = True
        json_encoders = {
            # custom output conversion for datetime
            datetime: custom_datetime_format
        }


class MemInfo(Base):
    __tablename__ = "meminfos"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    created = Column(DateTime, default=datetime.now, unique=True, index=True)
    total = Column(Integer)
    used = Column(Integer)
    free = Column(Integer)
