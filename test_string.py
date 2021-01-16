import pytest


def test_capitalize_method(test_data_string):
    new_string = test_data_string.capitalize()
    assert new_string[0].isupper()


@pytest.mark.parametrize("letter, count", [("a", 5), ("b", 2), ("c", 1), ("x", 0)])
def test_count_method(test_data_string, letter, count):
    assert test_data_string.count(letter) == count


def test_is_alpha_method(test_data_string):
    assert test_data_string.isalpha()


def test_startswith_method(test_data_string):
    assert test_data_string.startswith("a")


def index_method(test_data_string):
    assert test_data_string.index("a") == 0