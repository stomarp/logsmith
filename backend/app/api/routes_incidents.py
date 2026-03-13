from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.base import SessionLocal
from app.services.log_service import get_incident_candidates

router = APIRouter(prefix="/incidents", tags=["incidents"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
def get_incidents(
    slow_latency_threshold: int = Query(1000),
    db: Session = Depends(get_db),
):
    incidents = get_incident_candidates(
        db=db,
        slow_latency_threshold=slow_latency_threshold,
    )

    return {
        "count": len(incidents),
        "incidents": [
            {
                "id": str(log.id),
                "timestamp": log.timestamp.isoformat() if log.timestamp else None,
                "service": log.service,
                "level": log.level,
                "trace_id": log.trace_id,
                "endpoint": log.endpoint,
                "status_code": log.status_code,
                "latency_ms": log.latency_ms,
                "message": log.message,
                "metadata": log.log_metadata,
                "incident_type": (
                    "error" if log.status_code and log.status_code >= 500 else "slow_request"
                ),
            }
            for log in incidents
        ],
    }