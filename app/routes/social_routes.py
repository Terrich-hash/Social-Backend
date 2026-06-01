from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import SessionLocal
from app.models import Like, Comment, Follow, Post, User
from app.core.security import get_current_user
from app.schemas import CommentCreate

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/like/{post_id}")
def like(
    post_id: int,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    existing_like = (
        db.query(Like)
        .filter(
            Like.user_id == user_id,
            Like.post_id == post_id
        )
        .first()
    )

    if existing_like:
        raise HTTPException(status_code=400, detail="Already liked")

    db.add(
        Like(
            user_id=user_id,
            post_id=post_id
        )
    )

    db.commit()

    return {"msg": "liked"}


@router.post("/comment/{post_id}")
def comment(
    post_id: int,
    data: CommentCreate,
    user_id: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    comment = Comment(
        user_id=user_id,
        post_id=post_id,
        content=data.content
    )

    db.add(comment)
    db.commit()

    return {"msg": "commented"}


@router.post("/follow/{user_id}")
def follow(
    user_id: int,
    current: int = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    if current == user_id:
        raise HTTPException(
            status_code=400,
            detail="You cannot follow yourself"
        )

    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    existing_follow = (
        db.query(Follow)
        .filter(
            Follow.follower_id == current,
            Follow.following_id == user_id
        )
        .first()
    )

    if existing_follow:
        raise HTTPException(
            status_code=400,
            detail="Already following"
        )

    db.add(
        Follow(
            follower_id=current,
            following_id=user_id
        )
    )

    db.commit()

    return {"msg": "followed"}