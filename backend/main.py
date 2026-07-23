from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from celery import Celery
import os

from core.database import SessionLocal, init_db, Document
from core.storage import LocalStorage

celery_app = Celery('tasks', broker='redis://redis:6379/0')

app = FastAPI(
    title="DocIntel API",
    version="0.3.0",
    description="API for Document Intelligence Platform"
)

storage = LocalStorage()

@app.on_event("startup")
def on_startup():
    init_db()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/health", tags=["System"])
async def health_check():
    return {"status": "ok", "message": "Backend is running"}

@app.post("/upload", tags=["Documents"])
async def upload_document(file: UploadFile = File(...), db: Session = Depends(get_db)):
    content = await file.read()
    
    try:
        file_path = storage.save_file(file.filename, content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save file: {str(e)}")
    
    new_doc = Document(
        filename=file.filename,
        file_path=file_path,
        status="uploaded"
    )
    db.add(new_doc)
    db.commit()
    db.refresh(new_doc)
    
    celery_app.send_task("tasks.process_document", args=[new_doc.id, file_path])
    
    return {
        "message": "File uploaded successfully. Processing started.",
        "document_id": new_doc.id,
        "status": new_doc.status
    }

@app.get("/documents/{doc_id}", tags=["Documents"])
async def get_document(doc_id: int, db: Session = Depends(get_db)):
    doc = db.query(Document).filter(Document.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return {
        "id": doc.id,
        "filename": doc.filename,
        "status": doc.status,
        "content": doc.content_json,
        "created_at": doc.created_at
    }
