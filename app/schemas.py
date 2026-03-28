from pydantic import BaseModel, EmailStr, field_validator


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    @field_validator("password")
    def validate_password(cls, v):
        if len(v) > 72:
            raise ValueError("Password too long (max 72 characters)")
        return v


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class PostCreate(BaseModel):
    caption: str
    image_url: str


class CommentCreate(BaseModel):
    content: str


#  Fix forward refs (Pydantic v2 safe)
for model in [UserCreate, UserLogin, PostCreate, CommentCreate]:
    model.model_rebuild()