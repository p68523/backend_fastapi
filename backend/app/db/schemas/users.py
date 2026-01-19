from pydantic import BaseModel, Field
from datetime import datetime, timezone

class UserBase(BaseModel):
    email: str
    username: str
    password: str

class UserCreate(UserBase):
    pass