from celery import Celery
from core.database import SessionLocal, Document
from core.parser.pymupdf_parser import PyMuPDFParser

app = Celery('tasks', broker='redis://redis:6379/0')

@app.task(name="tasks.test_worker")
def test_worker():
    return "Worker is ready!"

@app.task(name="tasks.process_document")
def process_document(document_id: int, file_path: str):
    db = SessionLocal()
    doc = db.query(Document).filter(Document.id == document_id).first()
    
    if not doc:
        db.close()
        return f"Document {document_id} not found in DB"
        
    try:
        doc.status = "processing"
        db.commit()
        
        parser = PyMuPDFParser()
        parsed_json = parser.parse(file_path)
        
        if "error" in parsed_json:
            raise Exception(parsed_json["error"])
        
        doc.content_json = parsed_json
        doc.status = "completed"
        db.commit()
        
        return f"Document {document_id} parsed successfully"
        
    except Exception as e:
        doc.status = "error"
        doc.content_json = {"error": str(e)}
        db.commit()
        return f"Error processing document {document_id}: {str(e)}"
    finally:
        db.close()
