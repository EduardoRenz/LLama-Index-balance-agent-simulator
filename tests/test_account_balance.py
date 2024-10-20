import unittest

from gateways.MockedAccountBalance import MockedAccountBalanceGateway


class TestAccountBalance(unittest.TestCase):

    def test_get_balance(self):
        gateway = MockedAccountBalanceGateway()
        result = gateway.get_balance(1, 'USD')
        self.assertEqual(result, 100.0)


if __name__ == '__main__':
    unittest.main()
