from working import convert
import pytest


def test_normal_hours():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_with_minutes():
    assert convert("9:30 AM to 5:45 PM") == "09:30 to 17:45"


def test_midnight_and_noon():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"


def test_invalid_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5 PM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:75 AM to 5 PM")


def test_wrong_format():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")


def test_missing_to():
    with pytest.raises(ValueError):
        convert("9 AM 5 PM")


def test_out_of_range():
    with pytest.raises(ValueError):
        convert("12:60 AM to 5 PM")
