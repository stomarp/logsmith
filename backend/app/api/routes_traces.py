from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.base import SessionLocal
from app.services.log_service import get_logs_by_trace_id

router = APIRouter(prefix="/traces", tags=["traces"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/{trace_id}")
def get_trace(trace_id: str, db: Session = Depends(get_db)):
    logs = get_logs_by_trace_id(db, trace_id)

    return {
        "trace_id": trace_id,
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