"""
Unit tests for user operations
"""
import pytest
from app.crud.user import UserCRUD
from app.schemas.user import UserCreate

def test_create_user(db):
    user_crud = UserCRUD(db)
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword",
        first_name="Test",
        last_name="User"
    )
    
    user = user_crud.create(user_data)
    assert user.email == "test@example.com"
    assert user.username == "testuser"
    assert user.first_name == "Test"
    assert user.last_name == "User"

def test_get_user(db):
    user_crud = UserCRUD(db)
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword"
    )
    
    created_user = user_crud.create(user_data)
    retrieved_user = user_crud.get(created_user.id)
    
    assert retrieved_user is not None
    assert retrieved_user.email == "test@example.com"

def test_authenticate_user(db):
    user_crud = UserCRUD(db)
    user_data = UserCreate(
        email="test@example.com",
        username="testuser",
        password="testpassword"
    )
    
    user_crud.create(user_data)
    authenticated_user = user_crud.authenticate("test@example.com", "testpassword")
    
    assert authenticated_user is not None
    assert authenticated_user.email == "test@example.com"
    
    # Test wrong password
    wrong_auth = user_crud.authenticate("test@example.com", "wrongpassword")
    assert wrong_auth is None
