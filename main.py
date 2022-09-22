import pytest


def always_returns_true():
    print("Hello")
    print ("kat's change #2")
    return True


def test_always_returns_true():
    assert always_returns_true()
