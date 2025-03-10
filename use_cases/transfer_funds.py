from entities.account import Account
from typing import Protocol

class AccountRepository(Protocol):
    """
    Account repository interface
    Methods:
    - get_account: Get account from repository
    - save_account: Save account to repository

    Note that implementation of this interface is found on the interface_adapters layer
    """
    def get_account(self, account_id: str) -> Account:
        pass

    def save_account(self, account: Account) -> None:
        pass

class TransferFunds:
    def __init__(self, account_repository: AccountRepository):
        self.account_repository = account_repository

    def transfer(self, from_account_id: str, to_account_id: str, amount: float):
        from_account = self.account_repository.get_account(from_account_id)
        to_account = self.account_repository.get_account(to_account_id)

        from_account.withdraw(amount)
        to_account.deposit(amount)

        self.account_repository.save_account(from_account)
        self.account_repository.save_account(to_account)
