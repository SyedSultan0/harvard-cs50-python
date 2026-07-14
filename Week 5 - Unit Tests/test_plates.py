from plates import is_valid



def test_length():
    assert is_valid("CS") == True
    assert is_valid("CS50") == True
    assert is_valid("C") == False
    assert is_valid("ABCDEFG") == False


def test_start_letters():
    assert is_valid("AA123") == True
    assert is_valid("1A123") == False
    assert is_valid("A1123") == False


def test_numbers():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS5A") == False


def test_symbols():
    assert is_valid("PI3.14") == False
    assert is_valid("CS,50") == False
