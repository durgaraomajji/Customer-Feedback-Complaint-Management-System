from pydantic import BaseModel, Field

from app.schemas.common import ORMModel, UTCDateTime


class CategoryCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=255)


class CategoryUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=2, max_length=100)
    description: str | None = Field(default=None, max_length=255)


class CategoryOut(ORMModel):
    id: int
    name: str
    description: str | None
    is_active: bool
    created_at: UTCDateTime
