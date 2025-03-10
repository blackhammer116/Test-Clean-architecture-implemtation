import pytest
from unittest.mock import MagicMock
from use_cases.transfer_funds import TransferFunds, AccountRepository
from entities.account import Account

def test_transfer_success():
    mock_repo = MagicMock(AccountRepository)

    from_account = Account("123", 1000)
    to_account = Account("456", 500)

    mock_repo.get_account.side_effect = lambda account_id: from_account if account_id == "123" else to_account
    mock_repo.save_account = MagicMock()

    use_case = TransferFunds(mock_repo)

    use_case.transfer("123", "456", 200)

    assert from_account.balance == 800
    assert to_account.balance == 700

    mock_repo.save_account.assert_any_call(from_account)
    mock_repo.save_account.assert_any_call(to_account)

def test_transfer_insufficient_funds():
    mock_repo = MagicMock(AccountRepository)

    from_account = Account("123", 100)
    to_account = Account("456", 500)

    mock_repo.get_account.side_effect = lambda account_id: from_account if account_id == "123" else to_account
    mock_repo.save_account = MagicMock()

    use_case = TransferFunds(mock_repo)

    with pytest.raises(ValueError, match="Insufficient balance."):
        use_case.transfer("123", "456", 200)
