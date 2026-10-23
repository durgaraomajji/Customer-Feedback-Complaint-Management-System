from pydantic import BaseModel, Field, field_validator

from app.core.constants import ComplaintStatus, Priority, Severity
from app.schemas.common import ORMModel, UTCDateTime
from app.utils.validators import validate_attachment_urls


class ComplaintCreate(BaseModel):
    title: str = Field(min_length=3, max_length=200)
    description: str = Field(min_length=5, max_length=10000)
    category_id: int
    priority: Priority = Priority.MEDIUM
    severity: Severity = Severity.MINOR
    attachment_urls: list[str] = Field(default_factory=list)
    customer_id: int | None = Field(default=None, description="Staff only: file on behalf of a customer")

    @field_validator("attachment_urls")
    @classmethod
    def _urls(cls, v: list[str]) -> list[str]:
        return validate_attachment_urls(v)


class ComplaintUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=3, max_length=200)
    description: str | None = Field(default=None, min_length=5, max_length=10000)
    category_id: int | None = None
    priority: Priority | None = None  # staff only
    severity: Severity | None = None  # staff only
    attachment_urls: list[str] | None = None

    @field_validator("attachment_urls")
    @classmethod
    def _urls(cls, v: list[str] | None) -> list[str] | None:
        return validate_attachment_urls(v) if v is not None else v


class StatusChangeRequest(BaseModel):
    status: ComplaintStatus
    note: str | None = Field(default=None, max_length=500)


class ComplaintOut(ORMModel):
    id: int
    reference_no: str
    customer_id: int
    category_id: int
    title: str
    description: str
    priority: Priority
    severity: Severity
    status: ComplaintStatus
    attachment_urls: list[str]
    assigned_agent_id: int | None
    created_at: UTCDateTime
    updated_at: UTCDateTime
    due_at: UTCDateTime
    resolved_at: UTCDateTime | None
    closed_at: UTCDateTime | None
    reopen_count: int
