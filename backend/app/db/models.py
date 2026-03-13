from sqlalchemy import Column, DateTime, Integer, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()


class LogRecord(Base):
    __tablename__ = "logs"

    id = Column(UUID(as_uuid=True), primary_key=True, server_default=func.gen_random_uuid())
    timestamp = Column(DateTime(timezone=True), nullable=False)
    service = Column(Text, nullable=False)
    level = Column(Text, nullable=False)
    trace_id = Column(Text, nullable=True)
    span_id = Column(Text, nullable=True)
    user_id = Column(Text, nullable=True)
    endpoint = Column(Text, nullable=True)
    status_code = Column(Integer, nullable=True)
    latency_ms = Column(Integer, nullable=True)
    message = Column(Text, nullable=False)
    log_metadata = Column("metadata", JSONB, nullable=True)