"""
User endpoints
"""
from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.crud.user import UserCRUD
from app.schemas.user import User, UserCreate, UserUpdate
from app.core.exceptions import NotFoundError

router = APIRouter()

@router.get("/", response_model=List[User])
async def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get list of users"""
    user_crud = UserCRUD(db)
    users = user_crud.get_multi(skip=skip, limit=limit)
    return users

@router.post("/", response_model=User, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    """Create new user"""
    user_crud = UserCRUD(db)
    
    # Check if user already exists
    if user_crud.get_by_email(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    
    if user_crud.get_by_username(user.username):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken"
        )
    
    return user_crud.create(user)

@router.get("/{user_id}", response_model=User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    """Get user by ID"""
    user_crud = UserCRUD(db)
    user = user_crud.get(user_id)
    if not user:
        raise NotFoundError("User not found")
    return user

@router.put("/{user_id}", response_model=User)
async def update_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    """Update user"""
    user_crud = UserCRUD(db)
    user = user_crud.update(user_id, user_update)
    if not user:
        raise NotFoundError("User not found")
    return user

@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Delete user"""
    user_crud = UserCRUD(db)
    if not user_crud.delete(user_id):
        raise NotFoundError("User not found")
    return {"message": "User deleted successfully"}
