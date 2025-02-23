from abc import ABC, abstractmethod
from typing import Dict

class UserRegisterInterface(ABC):
    
    @abstractmethod
    def registry(self, username: str, password: str) -> Dict:    
        pass
    