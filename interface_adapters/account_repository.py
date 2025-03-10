from entities.account import Account
from use_cases.transfer_funds import AccountRepository

class InMemoryAccountRepository(AccountRepository):
    """
    In-memory implementation of AccountRepository: stores accounts in memory
    Methods:
    - get_account: Get account from repository
    - save_account: Save account to repository

    Note that the methods defined in the use-case layer are implemented here
    """
    def __init__(self):
        self.accounts = {}

    def get_account(self, account_id: str) -> Account:
        if account_id not in self.accounts:
            raise ValueError(f"Account with ID: {account_id} not found.")
        return self.accounts[account_id]

    def save_account(self, account: Account) -> None:
        self.accounts[account.account_id] = account


# Initializing dummy accounts for simulation
# In a real-world scenario, this data would be fetched from a database
account_repo = InMemoryAccountRepository()
account_repo.save_account(Account("1234", 1000.0))
account_repo.save_account(Account("5678", 5000.0))