from fastapi import FastAPI
from routers import report

app = FastAPI()


app.include_router(report.router)


@app.get("/")
async def root():
    return {"message": "FastApi"}
