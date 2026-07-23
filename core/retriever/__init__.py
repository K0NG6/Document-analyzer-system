from abc import ABC, abstractmethod
from typing import List, Dict, Any

class Retriever(ABC):
    @abstractmethod
    def search(self, query: str) -> List[Dict[str, Any]]:
        pass

class MockRetriever(Retriever):
    def search(self, query: str) -> List[Dict[str, Any]]:
        return [{"score": 0.99, "content": f"Mock result for query: {query}"}]
