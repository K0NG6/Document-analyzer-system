from abc import ABC, abstractmethod
from typing import Dict, Any

class Parser(ABC):
    @abstractmethod
    def parse(self, file_path: str) -> Dict[str, Any]:
        pass

class MockParser(Parser):
    def parse(self, file_path: str) -> Dict[str, Any]:
        return {
            "metadata": {"filename": file_path, "parser": "MockParser"},
            "content": f"Mocked parsed text from {file_path}",
            "pages": []
        }
