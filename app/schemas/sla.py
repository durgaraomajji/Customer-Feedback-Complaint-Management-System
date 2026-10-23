from pydantic import BaseModel, Field

from app.core.constants import Priority
from app.schemas.common import ORMModel, UTCDateTime


class SLARuleOut(ORMModel):
    id: int
    priority: Priority
    resolution_hours: int


class SLARuleUpdate(BaseModel):
    resolution_hours: int = Field(ge=1, le=720)


class SLAStatusOut(BaseModel):
    complaint_id: int
    reference_no: str
    priority: Priority
    created_at: UTCDateTime
    due_at: UTCDateTime
    sla_hours: float
    state: str  # on_track | at_risk | breached | met
    is_breached: bool
    is_finished: bool
    time_remaining_seconds: int | None
    overdue_seconds: int | None
    resolution_duration_seconds: int | None


class SLACheckResult(BaseModel):
    approaching_notified: int
    breached_notified: int
