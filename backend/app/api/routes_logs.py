from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.base import SessionLocal
from app.services.log_service import get_filtered_logs

router = APIRouter(prefix="/logs", tags=["logs"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def get_logs(
    service: str | None = Query(None),
    level: str | None = Query(None),
    status_code: int | None = Query(None),
    trace_id: str | None = Query(None),
    db: Session = Depends(get_db),
):

    logs = get_filtered_logs(
        db=db,
        service=service,
        level=level,
        status_code=status_code,
        trace_id=trace_id,
    )

    return {
        "count": len(logs),
        "logs": [
            {
                "id": str(log.id),
                "timestamp": log.timestamp.isoformat() if log.timestamp else None,
                "service": log.service,
                "level": log.level,
                "trace_id": log.trace_id,
                "span_id": log.span_id,
                "user_id": log.user_id,
                "endpoint": log.endpoint,
                "status_code": log.status_code,
                "latency_ms": log.latency_ms,
                "message": log.message,
                "metadata": log.log_metadata,
            }
            for log in logs
        ],
    }