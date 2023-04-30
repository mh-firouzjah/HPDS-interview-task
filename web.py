from typing import Optional

from fastapi import Depends, FastAPI
from fastapi_utils.tasks import repeat_every
from sqlalchemy.orm import Session

import models
from logger_config import logger
from database import SessionLocal, Sessionmaker, engine
from utils import get_memory_info

app = FastAPI()


models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def meminfo_api(
    db: Session = Depends(get_db),
    n: Optional[int] = None,
) -> list[models.PydanticMemInfo]:
    """This will return memory info records for the each last 'n' minutes.
    (defaults to 1 minutes ago/the last record)"""
    # (n == None) -> bool => int & in (0, 1).
    # list[:0] -> []
    return (
        db.query(models.MemInfo)
        .order_by(models.MemInfo.created.desc())
        .limit(n or n == None)
        .all()
    )


async def record_meminfo(db: Session) -> None:
    try:
        meminfo = models.MemInfo(**get_memory_info())
        db.add(meminfo)
        db.commit()
    except Exception as err:
        logger.error(err)


@app.on_event("startup")
@repeat_every(
    seconds=60 * 1,
    logger=logger,
    wait_first=True,
)  # 1 minute, wait_first to prevent duplicate
async def record_meminfo_task() -> None:
    with Sessionmaker.context_session() as db:
        await record_meminfo(db)
