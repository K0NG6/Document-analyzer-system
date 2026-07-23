from typing import Dict, Any
from . import Parser

class DoclingParser(Parser):
    def parse(self, file_path: str) -> Dict[str, Any]:
        
        return {
            "metadata": {"parser": "Docling", "file_path": file_path},
            "content": f"Docling mock parsed content for {file_path} (uncomment real code to use)",
            "pages": []
        }
