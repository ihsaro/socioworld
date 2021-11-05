from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class LoginCredentials(BaseModel):
    username: str
    password: str


class TokenCreated(BaseModel):
    access_token: str
    token_type: str


class UserRegistrationDetails(BaseModel):
    first_name: str = Field(max_length=100, title="First name of user")
    last_name: str = Field(max_length=100, title="Last name of user")
    date_of_birth: Optional[date] = Field(title="Date of birth of user")
    email: EmailStr = Field(title="Email address of user")
    username: str = Field(title="Username of user")
    password: str = Field(title="Password of user")


class RegisteredUser(BaseModel):
    id: int
    first_name: str = Field(max_length=100, title="First name of user")
    last_name: str = Field(max_length=100, title="Last name of user")
    date_of_birth: Optional[date] = Field(title="Date of birth of user")
    email: EmailStr = Field(title="Email address of user")
    username: str = Field(title="Username of user")
