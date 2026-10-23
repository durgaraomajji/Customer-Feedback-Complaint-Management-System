from pydantic import BaseModel, Field

from app.schemas.common import ORMModel, UTCDateTime


class AssignRequest(BaseModel):
    agent_id: int
    reason: str | None = Field(default=None, max_length=255)


class AssignmentOut(ORMModel):
    id: int
    complaint_id: int
    agent_id: int
    assigned_by: int
    reason: str | None
    assigned_at: UTCDateTime
    unassigned_at: UTCDateTime | None
    is_active: bool
