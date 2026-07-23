from abc import ABC, abstractmethod
from typing import List

class Chunker(ABC):
    @abstractmethod
    def chunk(self, text: str) -> List[str]:
        pass

class MockChunker(Chunker):
    def chunk(self, text: str) -> List[str]:
        return [f"Chunk 1: {text[:20]}", f"Chunk 2: {text[20:40]}"]
