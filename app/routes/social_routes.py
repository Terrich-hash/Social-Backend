from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Like, Comment, Follow
from app.core.security import get_current_user
from app.schemas import CommentCreate

router = APIRouter()

def get_db():
    db = SessionLocal()
    try: yield db
    finally: db.close()

@router.post("/like/{post_id}")
def like(post_id: int, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    db.add(Like(user_id=user_id, post_id=post_id))
    db.commit()
    return {"msg": "liked"}

@router.post("/comment/{post_id}")
def comment(post_id: int, data: CommentCreate, user_id: int = Depends(get_current_user), db: Session = Depends(get_db)):
    db.add(Comment(user_id=user_id, post_id=post_id, content=data.content))
    db.commit()
    return {"msg": "commented"}

@router.post("/follow/{user_id}")
def follow(user_id: int, current: int = Depends(get_current_user), db: Session = Depends(get_db)):

    if current == user_id:
        raise HTTPException(status_code=400, detail="You cannot follow yourself")

    db.add(Follow(follower_id=current, following_id=user_id))
    db.commit()

    return {"msg": "followed"}