import pytest


def test_copy_method(test_data_list):
    copy_lst = test_data_list.copy()
    assert copy_lst == test_data_list


@pytest.mark.parametrize("index, element", [(0, 0), (1, 10), (2, 20)])
def test_insert_method(test_data_list, index, element):
    test_data_list.insert(index, element)
    assert test_data_list[index] == element


def test_append_method(test_data_list):
    test_data_list.append(6)
    assert test_data_list[len(test_data_list) - 1] == 6


def test_clear_method(test_data_list):
    test_data_list.clear()
    assert len(test_data_list) == 0


@pytest.mark.xfail(reason="wrong number")
def test_pop_method(test_data_list):
    element = test_data_list.pop(-1)
    assert element == 10
