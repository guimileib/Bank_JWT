from abc import abstractmethod
from typing import Dict

class BalanceEditorInterface:
    
    @abstractmethod
    def edit(self, user_id: int, new_balance: float) -> Dict:
        pass