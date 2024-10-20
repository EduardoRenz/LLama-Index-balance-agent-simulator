from abc import ABC, abstractmethod
from typing import Dict


class AccountBalanceGateway(ABC):
    @abstractmethod
    def get_balance(self, user_id: int, currency: str) -> Dict[str, float]:
        """Get user account balance for all currencies."""
        pass
