from datetime import datetime

from pydantic import BaseModel


def custom_datetime_format(dt: datetime):
    return dt.strftime("%Y-%m-%d %H:%M")


class MemInfo(BaseModel):
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
