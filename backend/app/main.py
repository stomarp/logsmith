from fastapi import FastAPI

from app.api.routes_ingest import router as ingest_router

app = FastAPI(title="Logsmith Backend", version="0.1.0")

app.include_router(ingest_router)


@app.get("/")
def root():
    return {"message": "Logsmith backend is running"}


@app.get("/health")
def health():
    return {"status": "ok"}