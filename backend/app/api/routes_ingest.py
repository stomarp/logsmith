from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.base import SessionLocal
from app.schemas.log_event import LogEvent
from app.services.log_service import insert_logs

router = APIRouter(prefix="/ingest", tags=["ingest"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("")
def ingest_logs(logs: list[LogEvent], db: Session = Depends(get_db)):
    ingested_count = insert_logs(db, logs)

    return {
        "message": "Logs saved successfully",
        "ingested_count": ingested_count,
    }