import pytest

from src.wallet import Wallet


@pytest.fixture
def full_wallet():
    '''Returns a Wallet instance with a balance of 20'''
    return Wallet(20)


