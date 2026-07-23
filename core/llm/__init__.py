from abc import ABC, abstractmethod

class LLM(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass

class MockLLM(LLM):
    def generate(self, prompt: str) -> str:
        return f"Mock LLM generated text for prompt: {prompt[:20]}..."
