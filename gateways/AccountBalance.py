from abc import ABC, abstractmethod
from typing import Dict


class AccountBalanceGateway(ABC):
    @abstractmethod
    def get_balance(self,  currency: str) -> Dict[str, float]:
        """Get user account balance for all currencies."""
        pass

    @abstractmethod
    def withdraw(self, amount: float, currency: str) -> None:
        """Withdraw from user account."""
        pass

    @abstractmethod
    def deposit(self, amount: float, currency: str) -> None:
        """Deposit to user account."""
        pass
