import sqlite3
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel

DATABASE_URL = "test.db"
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

conn = sqlite3.connect(DATABASE_URL)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/users")
async def read_users():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE id = 1")
    row = cursor.fetchone()
    if row is not None:
        return row
    else:
        print("조회 결과가 없습니다.")

# 회원가입
@app.post("/regMember")
async def create_user(request: Request):
    user = await request.json()
    print(user)
    username = user['username']
    email = user['email']
    password = user['password']
    cursor = conn.cursor()
    cursor.execute("INSERT INTO user (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    conn.commit()
    return {"message": "User created successfully!"}

@app.get("/user")
async def root():
    return {"name": "Myeong Seop", "age":34, "job":"developer", "gender":"Male"}

@app.get("/user2")
async def root():
    return {"name": "So Young", "age":27, "job":"Publisher", "gender":"Female"}


class User(BaseModel):
    id: int
    name: str
    email: str
    password: str

def fetch_user_by_email(email: str):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE email = ?", (email,))
    row = cursor.fetchone()
    if row is not None:
        user = User(id=row[0], name=row[1], email=row[2], password=row[3])
        return user
    else:
        return None

@app.post("/login")
async def login(request: Request):
    form_data = await request.json()
    print(form_data['username'])
    user = fetch_user_by_email(form_data['username'])
    print(user)
    if user is None:
        return {"error": "Invalid email or password"}
    elif user.password != form_data['password']:
        return {"error": "Invalid email or password"}
    else:
        return {"message": "Login successful","code":200}
