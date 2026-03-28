from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db import SessionLocal
from app.models import Post
from app.schemas import PostCreate
from app.core.security import get_current_user

router = APIRouter()   # ✅ REQUIRED


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/")
def create_post(
    data: PostCreate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    post = Post(
        user_id=user_id,
        image_url=data.image_url,
        caption=data.caption
    )
    db.add(post)
    db.commit()
    return {"msg": "post created"}


@router.get("/feed")
def get_feed(
    limit: int = 10,
    offset: int = 0,
    db: Session = Depends(get_db)
):
    posts = db.query(Post)\
        .order_by(Post.id.desc())\
        .limit(limit)\
        .offset(offset)\
        .all()

    return posts