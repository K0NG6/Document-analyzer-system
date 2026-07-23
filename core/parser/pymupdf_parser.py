from typing import Dict, Any
import fitz
from . import Parser

class PyMuPDFParser(Parser):
    def parse(self, file_path: str) -> Dict[str, Any]:
        try:
            doc = fitz.open(file_path)
            pages_data = []
            full_text = ""
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                text = page.get_text()
                full_text += text + "\n"
                pages_data.append({
                    "page_number": page_num + 1,
                    "text": text.strip()
                })
            
            return {
                "metadata": {
                    "total_pages": len(doc),
                    "file_path": file_path,
                    "parser": "PyMuPDF"
                },
                "content": full_text.strip(),
                "pages": pages_data
            }
        except Exception as e:
            return {"error": str(e), "metadata": {"parser": "PyMuPDF"}}
