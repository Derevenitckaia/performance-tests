from pydantic import BaseModel, Field, EmailStr, ConfigDict


class UserSchema(BaseModel):
    """Schema for user."""
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class GetUserResponseSchema(BaseModel):
    """Response schema for getting a user."""
    user: UserSchema


class CreateUserRequestSchema(BaseModel):
    """Request schema for creating a new user"""
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")
    phone_number: str = Field(alias="phoneNumber")


class CreateUserResponseSchema(BaseModel):
    """Response schema for creating a new user."""
    user: UserSchema