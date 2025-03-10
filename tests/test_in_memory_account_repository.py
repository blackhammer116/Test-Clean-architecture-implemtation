import pytest
from interface_adapters.account_repository import InMemoryAccountRepository
from entities.account import Account

def test_get_account():
    repository = InMemoryAccountRepository()
    account = Account("123", 1000)
    repository.save_account(account)

    # Test that account can be fetched correctly
    retrieved_account = repository.get_account("123")
    assert retrieved_account.account_id == "123"
    assert retrieved_account.balance == 1000

def test_account_not_found():
    repository = InMemoryAccountRepository()

    with pytest.raises(ValueError, match="Account with ID: 999 not found."):
        repository.get_account("999")  # Trying to get an account that doesn't exist
