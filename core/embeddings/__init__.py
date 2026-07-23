from abc import ABC, abstractmethod
from typing import List

class Embedder(ABC):
    @abstractmethod
    def embed(self, text: str) -> List[float]:
        pass

class MockEmbedder(Embedder):
    def embed(self, text: str) -> List[float]:
        return [0.1, 0.2, 0.3, 0.4, 0.5]
