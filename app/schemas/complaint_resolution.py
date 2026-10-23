from pydantic import BaseModel, Field

from app.schemas.common import ORMModel, UTCDateTime


class ResolveRequest(BaseModel):
    summary: str = Field(min_length=5, max_length=5000)
    root_cause: str | None = Field(default=None, max_length=5000)
    action_taken: str | None = Field(default=None, max_length=5000)


class CloseRequest(BaseModel):
    note: str | None = Field(default=None, max_length=500)


class ReopenRequest(BaseModel):
    reason: str = Field(min_length=3, max_length=500)


class ResolutionOut(ORMModel):
    id: int
    complaint_id: int
    resolved_by: int
    summary: str
    root_cause: str | None
    action_taken: str | None
    created_at: UTCDateTime
