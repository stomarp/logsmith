from fastapi import APIRouter

router = APIRouter(prefix="/logs", tags=["logs"])


@router.get("")
def get_logs():
    return {
        "logs": [
            {
                "timestamp": "2026-03-11T20:30:00Z",
                "service": "orders-service",
                "level": "ERROR",
                "trace_id": "trace-123",
                "endpoint": "POST /orders",
                "status_code": 500,
                "latency_ms": 742,
                "message": "Database timeout while creating order",
            },
            {
                "timestamp": "2026-03-11T20:31:10Z",
                "service": "orders-service",
                "level": "INFO",
                "trace_id": "trace-124",
                "endpoint": "GET /health",
                "status_code": 200,
                "latency_ms": 18,
                "message": "Health check successful",
            },
        ],
        "count": 2,
    }
