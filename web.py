from fastapi import FastAPI

app = FastAPI()

RECORDS = [
    {"id": 1, "date": "2023-04-30 12:31", "total": 16637, "used": 4486, "free": 7034},
    {"id": 2, "date": "2023-04-30 12:32", "total": 16637, "used": 4386, "free": 7134},
    {"id": 3, "date": "2023-04-30 12:33", "total": 16637, "used": 4426, "free": 7094},
    {"id": 4, "date": "2023-04-30 12:34", "total": 16637, "used": 4486, "free": 7034},
]


@app.get("/")
async def meminfo_api(number_of_records: int = 1):
    """This will return memory info records of 'number_of_records'."""
    return RECORDS[:number_of_records]
