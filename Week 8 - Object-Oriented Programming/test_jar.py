from jar import Jar
import pytest


def test_init():
    jar = Jar(10)
    assert jar.capacity == 10
    assert jar.size == 0


def test_str():
    jar = Jar()
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"


def test_deposit():
    jar = Jar(5)
    jar.deposit(2)
    assert jar.size == 2


def test_deposit_overflow():
    jar = Jar(5)

    with pytest.raises(ValueError):
        jar.deposit(6)


def test_withdraw():
    jar = Jar(5)
    jar.deposit(5)
    jar.withdraw(2)

    assert jar.size == 3


def test_invalid_capacity():
    with pytest.raises(ValueError):
        Jar(-1)
