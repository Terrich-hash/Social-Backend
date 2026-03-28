from fastapi import FastAPI
from app.routes import auth_routes, post_routes, social_routes
from app.core.exceptions import handler, AppException
from slowapi.middleware import SlowAPIMiddleware
from app.core.rate_limiter import limiter

app = FastAPI()

app.add_exception_handler(AppException, handler)
app.state.limiter = limiter
app.add_middleware(SlowAPIMiddleware)

app.include_router(auth_routes.router, prefix="/auth")
app.include_router(post_routes.router, prefix="/posts")
app.include_router(social_routes.router, prefix="/social")

from app.db import engine
from app.models import Base
Base.metadata.create_all(bind=engine)