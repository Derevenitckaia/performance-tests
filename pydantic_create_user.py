from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    """Schema for user."""
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

class CreateUserRequestSchema(BaseModel):
    """Request schema for creating a new user"""
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")

class CreateUserResponseSchema(BaseModel):
    """Response schema for creating a new user."""
    user: UserSchema
