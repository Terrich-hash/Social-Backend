from fastapi import FastAPI

from app.routes import auth_routes, post_routes, social_routes
from app.core.exceptions import handler, AppException
from app.core.rate_limiter import limiter

from slowapi.middleware import SlowAPIMiddleware

from app.db import Base, engine

# import models so SQLAlchemy registers tables
from app.models import User, Post, Like, Comment, Follow, Notification


app = FastAPI()

# create tables
print("TABLES FOUND:", Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)

# middleware
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

# exception handler
app.add_exception_handler(AppException, handler)

# routes
app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(post_routes.router, prefix="/posts", tags=["Posts"])
app.include_router(social_routes.router, prefix="/social", tags=["Social"])