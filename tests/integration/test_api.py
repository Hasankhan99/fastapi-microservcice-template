"""
Integration tests for API endpoints
"""
import pytest

@pytest.mark.asyncio
async def test_health_check(client):
    response = await client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

@pytest.mark.asyncio
async def test_create_user(client):
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpassword",
        "first_name": "Test",
        "last_name": "User"
    }
    
    response = await client.post("/api/v1/users/", json=user_data)
    assert response.status_code == 201
    
    data = response.json()
    assert data["email"] == "test@example.com"
    assert data["username"] == "testuser"

@pytest.mark.asyncio
async def test_get_users(client):
    # First create a user
    user_data = {
        "email": "test@example.com",
        "username": "testuser",
        "password": "testpassword"
    }
    await client.post("/api/v1/users/", json=user_data)
    
    # Then get users
    response = await client.get("/api/v1/users/")
    assert response.status_code == 200
    
    data = response.json()
    assert len(data) == 1
    assert data[0]["email"] == "test@example.com"
