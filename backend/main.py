from fastapi import FastAPI

app = FastAPI(
    title="DocIntel API",
    version="0.1.0",
    description="API for Document Intelligence Platform"
)

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "ok", "message": "Backend is running"}
