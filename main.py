import sqlite3
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# uvicorn main:app --reload 서버 시동
# sqllit3 에서 테이블이랑 db 조회해서 확인해보기

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

@app.post("/createMember")
async def root():
    return {"message": "Hello World"}

@app.post("/login")
async def root():
    return {"message": "Hello World"}

@app.get("/user")
async def root():
    return {"message": "Hello World"}