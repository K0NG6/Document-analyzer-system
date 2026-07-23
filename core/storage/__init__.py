import os
import uuid
from abc import ABC, abstractmethod

class Storage(ABC):
    @abstractmethod
    def save_file(self, filename: str, content: bytes) -> str:
        pass

    @abstractmethod
    def get_file(self, file_path: str) -> bytes:
        pass

class LocalStorage(Storage):
    def __init__(self, base_dir: str = "/app/data/uploads"):
        self.base_dir = base_dir
        os.makedirs(self.base_dir, exist_ok=True)

    def save_file(self, filename: str, content: bytes) -> str:
        unique_filename = f"{uuid.uuid4().hex}_{filename}"
        file_path = os.path.join(self.base_dir, unique_filename)
        
        with open(file_path, "wb") as f:
            f.write(content)
            
        return file_path

    def get_file(self, file_path: str) -> bytes:
        with open(file_path, "rb") as f:
            return f.read()
