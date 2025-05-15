from fastapi import FastAPI
from routers import report
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS beállítás a frontend alkalmazással való kommunikációhoz
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://your-frontend-domain.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(report.router)


@app.get("/")
async def root():
    return {"message": "FastApi"}
