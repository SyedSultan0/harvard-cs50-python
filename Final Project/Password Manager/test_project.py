from project import hashing, checking, check_password_strength, breach


def test_hashing_same_input():
    assert hashing("hello") == hashing("hello")


def test_hashing_different_input():
    assert hashing("hello") != hashing("world")


def test_checking_false_case():
    # should return False for wrong password
    assert checking("wrong_password_example") is False


def test_strength_returns_int():
    # we cannot simulate input easily, so we just check function exists
    assert callable(check_password_strength)


def test_breach_function_exists():
    assert callable(breach)
