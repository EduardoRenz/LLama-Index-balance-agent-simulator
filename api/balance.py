
from gateways.MockedAccountBalance import MockedAccountBalanceGateway


gateway = MockedAccountBalanceGateway()


def get_balance(currency: str):
    """Get user account balance for all currencies."""
    response = gateway.get_balance(1, currency.upper())
    return response
