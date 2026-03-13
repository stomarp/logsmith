from sqlalchemy.orm import Session

from app.db.models import LogRecord
from app.schemas.log_event import LogEvent


def insert_logs(db: Session, logs: list[LogEvent]) -> int:
    records = [
        LogRecord(
            timestamp=log.timestamp,
            service=log.service,
            level=log.level,
            trace_id=log.trace_id,
            span_id=log.span_id,
            user_id=log.user_id,
            endpoint=log.endpoint,
            status_code=log.status_code,
            latency_ms=log.latency_ms,
            message=log.message,
            log_metadata=log.metadata,
        )
        for log in logs
    ]

    db.add_all(records)
    db.commit()

    return len(records)