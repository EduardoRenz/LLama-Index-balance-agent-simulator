from typing import Dict
from gateways.AccountBalance import AccountBalanceGateway


class MockedAccountBalanceGateway(AccountBalanceGateway):
    """Mocked AccountBalanceGateway for testing purposes."""

    balance = {"USD": 100.0, "EUR": 80.0, "GBP": 70.0}

    def get_balance(self, user_id: int, currency: str) -> Dict[str, float]:
        """Get user account balance for all currencies."""
        if (currency not in self.balance):
            raise ValueError(f"Currency {currency} is not supported.")

        return self.balance[currency]
