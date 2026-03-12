from fastapi import FastAPI

app = FastAPI(title="Logsmith Backend", version="0.1.0")


@app.get("/")
def root():
    return {"message": "Logsmith backend is running"}


@app.get("/health")
def health():
    return {"status": "ok"}