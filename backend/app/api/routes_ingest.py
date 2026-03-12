from fastapi import APIRouter

from app.schemas.log_event import LogEvent

router = APIRouter(prefix="/ingest", tags=["ingest"])


@router.post("")
def ingest_logs(logs: list[LogEvent]):
    return {
        "message": "Logs received successfully",
        "ingested_count": len(logs),
        "sample_service": logs[0].service if logs else None,
    }
