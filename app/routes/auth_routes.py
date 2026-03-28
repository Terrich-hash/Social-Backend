from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.db import SessionLocal
from app.models import User
from app.schemas import UserCreate, UserLogin
from passlib.hash import bcrypt
from jose import jwt
import os

router = APIRouter()

SECRET = os.getenv("SECRET_KEY", "mysecret")  # fallback


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- REGISTER ----------------
@router.post("/register")
def register(data: UserCreate, db: Session = Depends(get_db)):
    user = User(
        username=data.username,
        email=data.email,
        password=bcrypt.hash(data.password[:72])
    )

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="Username or email already exists")

    return {"msg": "user created"}


# ---------------- LOGIN ----------------
@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == data.email).first()

    if not user or not bcrypt.verify(data.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = jwt.encode({"user_id": user.id}, SECRET, algorithm="HS256")

    return {"access_token": token}