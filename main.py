import pytest


def always_returns_true():
    return True
print("you are completely correct")

def test_always_returns_true():
    assert always_returns_true()
