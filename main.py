from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import fruits


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(fruits.router, prefix="/fruits")


@app.get("/")
async def root():
    return {"message": "Hello World"}
