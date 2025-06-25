"""
Authentication endpoints
"""
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.crud.user import UserCRUD
from app.core.security.jwt import create_access_token, verify_token
from app.core.exceptions import UnauthorizedError

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/token")
async def login(form_data: dict = Depends(OAuth2PasswordRequestForm), db: Session = Depends(get_db)):
    """Login user and return access token"""
    user_crud = UserCRUD(db)
    user = user_crud.authenticate(form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/me")
async def read_users_me(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    """Get current user"""
    payload = verify_token(token)
    if not payload:
        raise UnauthorizedError("Invalid token")
    
    email = payload.get("sub")
    if not email:
        raise UnauthorizedError("Invalid token")
    
    user_crud = UserCRUD(db)
    user = user_crud.get_by_email(email)
    if not user:
        raise UnauthorizedError("User not found")
    
    return user
