"""
This is the main contorller of the application ie. the frameworks and driver layer
"""

from use_cases.transfer_funds import TransferFunds
from interface_adapters.account_repository import InMemoryAccountRepository
from entities.account import Account

account_repo = InMemoryAccountRepository()
transfer_use_case = TransferFunds(account_repository=account_repo)

account_repo.save_account(Account("1234", 1000.0))
account_repo.save_account(Account("5678", 5000.0))

try:
    transfer_use_case.transfer(from_account_id="1234", to_account_id="5678", amount=500.0)
    print("Transfer successful")
except ValueError as e:
    print(f"Transfer failed: {str(e)}")

from_account = account_repo.get_account("1234")
to_account = account_repo.get_account("5678")
print(f"From account balance: {from_account.balance}")
print(f"To account balance: {to_account.balance}")