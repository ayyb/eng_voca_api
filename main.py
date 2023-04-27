import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

conn = sqlite3.connect('test.db')
c = conn.cursor()
app = FastAPI()

# CORS 설정
origins = [
    "http://localhost",
    "http://localhost:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}