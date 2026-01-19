from fastapi import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services import UserService