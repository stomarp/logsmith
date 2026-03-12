from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class LogEvent(BaseModel):
    timestamp: datetime
    service: str = Field(..., min_length=1)
    level: str = Field(..., min_length=1)
    trace_id: str | None = None
    span_id: str | None = None
    user_id: str | None = None
    endpoint: str | None = None
    status_code: int | None = None
    latency_ms: int | None = None
    message: str = Field(..., min_length=1)
    metadata: dict[str, Any] | None = None