from um import count


def test_single_um():
    assert count("hello, um, world") == 1


def test_case_insensitive():
    assert count("Um, thanks for the album.") == 1


def test_punctuation():
    assert count("um? um! (um)") == 3


def test_not_substring():
    assert count("yummy umbrella") == 0
