from bank import value


def test_lowercase():
    assert value("hello,iam syed") == 0
    assert value("hey") == 20
    assert value("whatsup!") == 100

def test_uppercase():
    assert value("HELLO,IAM SYED") == 0
    assert value("HEY") == 20
    assert value("WHATSUP") == 100

def test_randomcase():
    assert value("123") == 100
    assert value("!)@_!#") == 100
    assert value("h123241") == 20
