import pytest


@pytest.mark.parametrize("name, house", [("Harry Potter", "Gryffindor"), ("Newton Scalamander", "Hufferpuff"),
                                         pytest.param("Hermione Granger", "Gryffindor",
                                         marks=pytest.mark.xfail(reason="non-existent key"))])
def test_get_value(test_data_dict, name, house):
    assert test_data_dict.get(name) == house


def test_get_all_keys(test_data_dict):
    keys = list(test_data_dict.keys())
    assert keys == ['Harry Potter', 'Newton Scalamander', 'Draco Malfoy']


def test_get_all_values(test_data_dict):
    values = list(test_data_dict.values())
    assert values == ["Gryffindor", "Hufferpuff", "Slytherin"]


def test_add_new_pair(test_data_dict):
    initial_length = len(test_data_dict)
    test_data_dict.update({"Luna Lovegood": "Ravenclaw"})
    new_length = len(test_data_dict)
    assert new_length - initial_length == 1


def test_delete_last_pair(test_data_dict):
    initial_length = len(test_data_dict)
    test_data_dict.popitem()
    new_length = len(test_data_dict)
    assert initial_length - new_length == 1

