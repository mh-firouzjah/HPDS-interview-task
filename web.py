from typing import Optional

from fastapi import FastAPI
from fastapi_utils.tasks import repeat_every

app = FastAPI()

RECORDS = [
    {"id": 1, "date": "2023-04-30 12:31", "total": 16637, "used": 4486, "free": 7034},
    {"id": 2, "date": "2023-04-30 12:32", "total": 16637, "used": 4386, "free": 7134},
    {"id": 3, "date": "2023-04-30 12:33", "total": 16637, "used": 4426, "free": 7094},
    {"id": 4, "date": "2023-04-30 12:34", "total": 16637, "used": 4486, "free": 7034},
]


@app.get("/")
async def meminfo_api(n: Optional[int] = None):
    """This will return memory info records for the each last 'n' minutes.(defaults to 1 minutes ago/1 record)"""
    # n == None returns a boolean which is it self an integer either 0 or 1.
    # list[:0] -> []
    return RECORDS[: n or n == None]


async def record_meminfo():
    from datetime import datetime

    RECORDS.append(
        {
            "id": RECORDS[-1]["id"] + 1,
            "date": str(datetime.now())[:16],
            "total": 16637,
            "used": 4486,
            "free": 7034,
        }
    )


@app.on_event("startup")
@repeat_every(seconds=60 * 1)  # 1 minute
async def record_meminfo_task() -> None:
    return await record_meminfo()
