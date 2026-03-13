from sqlalchemy import select
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


def get_filtered_logs(
    db: Session,
    service: str | None = None,
    level: str | None = None,
    status_code: int | None = None,
    trace_id: str | None = None,
) -> list[LogRecord]:

    stmt = select(LogRecord)

    if service:
        stmt = stmt.where(LogRecord.service == service)

    if level:
        stmt = stmt.where(LogRecord.level == level)

    if status_code:
        stmt = stmt.where(LogRecord.status_code == status_code)

    if trace_id:
        stmt = stmt.where(LogRecord.trace_id == trace_id)

    stmt = stmt.order_by(LogRecord.timestamp.desc())

    result = db.execute(stmt)

    return result.scalars().all()


def get_logs_by_trace_id(db: Session, trace_id: str) -> list[LogRecord]:
    stmt = (
        select(LogRecord)
        .where(LogRecord.trace_id == trace_id)
        .order_by(LogRecord.timestamp.asc())
    )
    result = db.execute(stmt)
    return result.scalars().all()

def get_incident_candidates(
    db: Session,
    slow_latency_threshold: int = 1000,
) -> list[LogRecord]:
    stmt = (
        select(LogRecord)
        .where(
            (LogRecord.status_code >= 500) |
            (LogRecord.latency_ms >= slow_latency_threshold)
        )
        .order_by(LogRecord.timestamp.desc())
    )

    result = db.execute(stmt)
    return result.scalars().all()