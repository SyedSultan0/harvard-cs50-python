from numb3rs import validate


def test_range():
    assert validate("1.1.1.1") == True
    assert validate("255.255.255.255") == True
    assert validate("256.1.1.1") == False
    assert validate("1.999.1.1") == False


def test_string():
    assert validate("cat.1.1.1") == False
    assert validate("1.two.1.1") == False


def test_parts():
    assert validate("1.1.1") == False
    assert validate("1.1.1.1.1") == False


def test_zero():
    assert validate("000.001.010.100") == False
