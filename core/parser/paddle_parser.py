from typing import Dict, Any
from . import Parser

class PaddleOCRParser(Parser):
    def parse(self, file_path: str) -> Dict[str, Any]:
        return {
            "metadata": {"parser": "PaddleOCR", "file_path": file_path},
            "content": f"PaddleOCR mock extracted text for {file_path}",
            "pages": []
        }
