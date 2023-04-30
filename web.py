from datetime import datetime
from typing import Optional

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

from config import logger
from models import MemInfo
from utils import get_memory_info

app = FastAPI()

RECORDS = [
    {
        "id": 1,
        "created": datetime.now(),
        "total": 16637,
        "used": 4486,
        "free": 7034,
    },
    {
        "id": 2,
        "created": datetime.now(),
        "total": 16637,
        "used": 4386,
        "free": 7134,
    },
    {
        "id": 3,
        "created": datetime.now(),
        "total": 16637,
        "used": 4426,
        "free": 7094,
    },
    {
        "id": 4,
        "created": datetime.now(),
        "total": 16637,
        "used": 4486,
        "free": 7034,
    },
]


@app.get("/")
async def meminfo_api(n: Optional[int] = None) -> list[MemInfo]:
    """This will return memory info records for the each last 'n' minutes.(defaults to 1 minutes ago/1 record)"""
    # (n == None) -> bool => int & in (0, 1).
    # list[:0] -> []
    return list(reversed(RECORDS))[: n or n == None]


async def record_meminfo():
    try:
        get_memory_info()
    except Exception as err:
        logger.error(err)


@app.on_event("startup")
@repeat_every(seconds=60 * 1, logger=logger)  # 1 minute
async def record_meminfo_task() -> None:
    await record_meminfo()
