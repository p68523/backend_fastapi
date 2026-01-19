from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from app.db.models import User
from app.db.schemas.users import UserCreate

class UserService:
    pass