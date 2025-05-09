from builtins import str
import pytest
from pydantic import ValidationError
from datetime import datetime
from app.schemas.user_schemas import UserBase, UserCreate, UserUpdate, UserResponse, UserListResponse, LoginRequest

# Tests for UserBase
def test_user_base_valid(user_base_data):
    user = UserBase(**user_base_data)
    assert user.nickname == user_base_data["nickname"]
    assert user.email == user_base_data["email"]

# Tests for UserCreate
def test_user_create_valid(user_create_data):
    user = UserCreate(**user_create_data)
    assert user.nickname == user_create_data["nickname"]
    assert user.password == user_create_data["password"]

# Tests for UserUpdate
def test_user_update_valid(user_update_data):
    user_update = UserUpdate(**user_update_data)
    assert user_update.email == user_update_data["email"]
    assert user_update.first_name == user_update_data["first_name"]

# Tests for UserResponse
def test_user_response_valid(user_response_data):
    user = UserResponse(**user_response_data)
    assert user.id == user_response_data["id"]
    assert user.last_login_at == user_response_data["last_login_at"]

# Tests for LoginRequest
def test_login_request_valid(login_request_data):
    login = LoginRequest(**login_request_data)
    assert login.email == login_request_data["email"]
    assert login.password == login_request_data["password"]

# Parametrized tests for nickname and email validation
@pytest.mark.parametrize("nickname", ["test_user", "test-user", "testuser123", "123test"])
def test_user_base_nickname_valid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    user = UserBase(**user_base_data)
    assert user.nickname == nickname

@pytest.mark.parametrize("nickname", ["test user", "test?user", "", "us"])
def test_user_base_nickname_invalid(nickname, user_base_data):
    user_base_data["nickname"] = nickname
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Parametrized tests for URL validation
@pytest.mark.parametrize("url", ["http://valid.com/profile.jpg", "https://valid.com/profile.png", None])
def test_user_base_url_valid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    user = UserBase(**user_base_data)
    assert user.profile_picture_url == url

@pytest.mark.parametrize("url", ["ftp://invalid.com/profile.jpg", "http//invalid", "https//invalid"])
def test_user_base_url_invalid(url, user_base_data):
    user_base_data["profile_picture_url"] = url
    with pytest.raises(ValidationError):
        UserBase(**user_base_data)

# Tests for UserBase invalid email
def test_user_base_invalid_email(user_base_data_invalid):
    with pytest.raises(ValidationError) as exc_info:
        user = UserBase(**user_base_data_invalid)
    assert "value is not a valid email address" in str(exc_info.value)
    assert "john.doe.example.com" in str(exc_info.value)

# Schema example data match between registration and login
def test_user_create_and_login_example_match():
    user_create_schema = UserCreate.schema()
    login_schema = LoginRequest.schema()
    assert user_create_schema['properties']['email']['example'] == login_schema['properties']['email']['example']
    assert user_create_schema['properties']['password']['example'] == login_schema['properties']['password']['example']

# Password validation tests
@pytest.mark.parametrize("bad_password", [
    "short",               # too short
    "nocapital123!",       # no uppercase
    "NOLOWERCASE123!",     # no lowercase
    "NoSpecials123",       # no special character
    "NoDigits!"            # no digits
])
def test_user_create_invalid_passwords(user_base_data, bad_password):
    data = {**user_base_data, "password": bad_password}
    with pytest.raises(ValidationError):
        UserCreate(**data)

def test_user_create_valid_password(user_base_data):
    data = {**user_base_data, "password": "ValidPass123!"}
    user = UserCreate(**data)
    assert user.password == "ValidPass123!"

# Whitespace stripping validation
def test_user_base_strips_whitespace(user_base_data):
    user_base_data["first_name"] = "  John  "
    user_base_data["last_name"] = "  Doe "
    user_base_data["nickname"] = " john_doe "
    user_base_data["bio"] = "  Backend dev  "
    user_base_data["linkedin_profile_url"] = "  https://linkedin.com/in/johndoe  "
    user_base_data["github_profile_url"] = "  https://github.com/johndoe  "
    
    user = UserBase(**user_base_data)

    assert user.first_name == "John"
    assert user.last_name == "Doe"
    assert user.nickname == "john_doe"
    assert user.bio == "Backend dev"
    assert user.linkedin_profile_url == "https://linkedin.com/in/johndoe"
    assert user.github_profile_url == "https://github.com/johndoe"