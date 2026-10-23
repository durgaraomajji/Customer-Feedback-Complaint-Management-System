from pydantic import BaseModel, Field

from app.schemas.common import ORMModel, UTCDateTime


class CommentCreate(BaseModel):
    body: str = Field(min_length=1, max_length=5000)
    is_internal: bool = Field(default=False, description="Internal notes are visible to staff only")


class CommentOut(ORMModel):
    id: int
    complaint_id: int
    author_id: int
    body: str
    is_internal: bool
    created_at: UTCDateTime
