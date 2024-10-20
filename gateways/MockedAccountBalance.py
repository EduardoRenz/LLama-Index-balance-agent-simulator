from typing import Dict
from gateways.AccountBalance import AccountBalanceGateway


class MockedAccountBalanceGateway(AccountBalanceGateway):
    """Mocked AccountBalanceGateway for testing purposes."""

    balance = {"USD": 300.0, "EUR": 80.0, "GBP": 70.0}

    def get_balance(self, currency: str) -> Dict[str, float]:
        """Get user account balance for all currencies."""
        if (currency.upper() not in self.balance):
            raise ValueError(f"Currency {currency} is not supported.")

        return self.balance[currency.upper()]

    def withdraw(self, amount: str, currency: str) -> None:
        float_amount = float(amount)
        """Withdraw from user account."""
        if (currency.upper() not in self.balance):
            raise ValueError(f"Currency {currency.upper()} is not supported.")

        if (self.balance[currency.upper()] - float_amount < 0):
            raise ValueError("Not enough balance.")

        self.balance[currency.upper()] -= float_amount
        return f"Withdrawal successful. your new balance of {currency.upper()} is {self.balance[currency.upper()]}"

    def deposit(self, amount: str, currency: str) -> None:
        float_amount = float(amount)
        """Deposit to user account."""
        if (currency.upper() not in self.balance):
            raise ValueError(f"Currency {currency.upper()} is not supported.")

        self.balance[currency.upper()] += float_amount
        return f"Deposit successful. your new balance is {self.balance[currency.upper()]}"
