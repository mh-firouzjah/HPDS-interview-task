from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def meminfo_api(number_of_records: int = 1):
    """This will return memory info records of 'number_of_records'."""
    return {"meminfo": "no thing yet!"}
