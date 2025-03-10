from entities.account import Account
import pytest


def test_deposit():
    account = Account("1234", 1000.0)
    account.deposit(500.0)
    assert account.balance == 1500.0


def test_withdraw():
    account = Account("1234", 1000.0)
    account.withdraw(500.0)
    assert account.balance == 500.0


def test_withdraw_insufficient_balance():
    account = Account("1234", 1000.0)
    with pytest.raises(ValueError, match="Insufficient balance."):
        account.withdraw(1500.0)


def test_deposit_negative_amount():
    account = Account("1234", 1000.0)
    with pytest.raises(ValueError, match="Deposit amount must be greater than 0"):
        account.deposit(-500.0)