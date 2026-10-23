from pydantic import BaseModel, EmailStr, Field, field_validator

from app.utils.validators import validate_password_strength


class RegisterRequest(BaseModel):
    email: EmailStr
    full_name: str = Field(min_length=2, max_length=150)
    password: str
    phone: str | None = Field(default=None, max_length=30)

    @field_validator("email")
    @classmethod
    def _lower(cls, v: str) -> str:
        return v.lower()

    @field_validator("password")
    @classmethod
    def _password(cls, v: str) -> str:
        return validate_password_strength(v)


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
    expires_in: int


class RefreshRequest(BaseModel):
    refresh_token: str
