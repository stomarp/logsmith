from fastapi import FastAPI

from app.api.routes_ingest import router as ingest_router
from app.api.routes_logs import router as logs_router
from app.api.routes_traces import router as traces_router

app = FastAPI(title="Logsmith Backend", version="0.1.0")

app.include_router(ingest_router)
app.include_router(logs_router)
app.include_router(traces_router)

@app.get("/")
def root():
    return {"message": "Logsmith backend is running"}


@app.get("/health")
def health():
    return {"status": "ok"}