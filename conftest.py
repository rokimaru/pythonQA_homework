import pytest


@pytest.fixture(scope="function")
def test_data_list():
    return [1, 2, 3, 4, 5]


@pytest.fixture(scope="function")
def test_data_dict():
    return {"Harry Potter": "Gryffindor", "Newton Scalamander": "Hufferpuff", "Draco Malfoy": "Slytherin"}


@pytest.fixture(scope="function")
def test_data_set():
    return {"apple", "orange", "banana"}


@pytest.fixture(scope="function")
def test_data_string():
    return "abracadabra"
