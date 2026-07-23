from abc import ABC, abstractmethod
from typing import List, Dict, Any

class VectorDB(ABC):
    @abstractmethod
    def save(self, collection_name: str, vectors: List[List[float]], payloads: List[Dict[str, Any]]):
        pass

class MockVectorDB(VectorDB):
    def save(self, collection_name: str, vectors: List[List[float]], payloads: List[Dict[str, Any]]):
        print(f"Saved {len(vectors)} vectors to {collection_name}")
