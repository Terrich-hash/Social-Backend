from sqlalchemy import Column, Integer, String, ForeignKey, Text, TIMESTAMP, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db import Base
from sqlalchemy import UniqueConstraint


# ---------------- USER ----------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    # relationships
    posts = relationship("Post", back_populates="user", cascade="all, delete")
    comments = relationship("Comment", back_populates="user", cascade="all, delete")


# ---------------- POST ----------------
class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    image_url = Column(String(500))
    caption = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())

    # relationships
    user = relationship("User", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete")


# ---------------- LIKE ----------------
class Like(Base):
    __tablename__ = "likes"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"))
    #prevent duplicate likes
    __table_args__ = (
    UniqueConstraint('user_id', 'post_id', name='unique_like'),
)

# ---------------- COMMENT ----------------
class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    post_id = Column(Integer, ForeignKey("posts.id", ondelete="CASCADE"))
    content = Column(Text, nullable=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

    # relationships
    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")


# ---------------- FOLLOW ----------------
class Follow(Base):
    __tablename__ = "followers"

    follower_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    following_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), primary_key=True)
    
# ---------------- NOTIFICATION ----------------
class Notification(Base):
    __tablename__ = "notifications"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    message = Column(Text)
    is_read = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, server_default=func.now())

