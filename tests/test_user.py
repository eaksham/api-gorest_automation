"""
test_users.py:
This file contains API tests for user operations such as Create, Read, Update, and Delete.
"""

import pytest
import allure

@allure.feature("User API")
@allure.story("Create a new user")
def test_create_user(api_client):
    """
    Test the creation of a new user using the API.
    """
    data = {
        "name": "Test User",
        "email": "test.user@example.com",
        "gender": "male",
        "status": "active"
    }
    response = api_client.post("/users", data)
    assert response.status_code == 201
    assert response.json()["name"] == data["name"]

@allure.feature("User API")
@allure.story("Get all users")
def test_get_users(api_client):
    """
    Test retrieving the list of users.
    """
    response = api_client.get("/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
