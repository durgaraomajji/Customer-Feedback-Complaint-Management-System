from pydantic import BaseModel, Field

from app.core.constants import FeedbackStatus
from app.schemas.common import ORMModel, UTCDateTime


class FeedbackCreate(BaseModel):
    category_id: int
    rating: int = Field(ge=1, le=5, description="Rating from 1 (worst) to 5 (best)")
    description: str = Field(min_length=3, max_length=5000)
    complaint_id: int | None = Field(default=None, description="Optional: link to your resolved/closed complaint")
    customer_id: int | None = Field(default=None, description="Staff only: submit on behalf of a customer")


class FeedbackUpdate(BaseModel):
    category_id: int | None = None
    rating: int | None = Field(default=None, ge=1, le=5)
    description: str | None = Field(default=None, min_length=3, max_length=5000)


class FeedbackStatusUpdate(BaseModel):
    status: FeedbackStatus


class FeedbackOut(ORMModel):
    id: int
    customer_id: int
    category_id: int
    complaint_id: int | None
    rating: int
    description: str
    status: FeedbackStatus
    feedback_date: UTCDateTime
    updated_at: UTCDateTime
