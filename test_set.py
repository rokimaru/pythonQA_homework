import pytest


@pytest.mark.parametrize("element", ["pear", "melon", "cranberry"])
def test_add_method(test_data_set, element):
    test_data_set.add(element)
    assert element in test_data_set


def test_remove_method(test_data_set):
    test_data_set.remove("apple")
    assert "apple" not in test_data_set


def test_pop_method(test_data_set):
    initial_length = len(test_data_set)
    test_data_set.pop()
    new_length = len(test_data_set)
    assert initial_length - new_length == 1


def test_intersection_method(test_data_set):
    another_set = {"carrot", "apple", "cabbage"}
    assert test_data_set.intersection(another_set) == {"apple"}


def test_union_method(test_data_set):
    another_set = {"carrot", "apple", "cabbage"}
    assert test_data_set.union(another_set) == {"carrot", "orange", "banana", "cabbage", "apple"}
