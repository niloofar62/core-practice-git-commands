import pytest


def always_returns_true():
    print("Hello")
    print ("kat's change #2")
    print("change 3")
    return True

print("wwwwww")
def test_always_returns_true():
    assert always_returns_true()
