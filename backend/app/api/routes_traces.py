from fastapi import APIRouter

router = APIRouter(prefix="/traces", tags=["traces"])


@router.get("/{trace_id}")
def get_trace(trace_id: str):
    return {
        "trace_id": trace_id,
        "logs": [
            {
                "timestamp": "2026-03-11T20:30:00Z",
                "service": "orders-service",
                "level": "INFO",
                "message": "Received order request",
            },
            {
                "timestamp": "2026-03-11T20:30:01Z",
                "service": "orders-service",
                "level": "INFO",
                "message": "Attempting database insert",
            },
            {
                "timestamp": "2026-03-11T20:30:02Z",
                "service": "orders-service",
                "level": "ERROR",
                "message": "Database timeout while creating order",
            },
        ],
        "count": 3,
    }