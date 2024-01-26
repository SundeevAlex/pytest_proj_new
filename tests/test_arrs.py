import pytest
from utils import arrs


@pytest.fixture
def array_fixture():
    return [1, 2, 3, 4]


def test_get(array_fixture):
    assert arrs.get(array_fixture, 1, "test") == 2
    assert arrs.get(array_fixture[0:0], 0, "test") == "test"


def test_slice(array_fixture):
    assert arrs.my_slice(array_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture[0:-1], 1) == [2, 3]
    assert arrs.my_slice(array_fixture[0:0]) == []
    assert arrs.my_slice(array_fixture[0:-1]) == [1, 2, 3]


# def test_get():
#     assert arrs.get([1, 2, 3], 1, "test") == 2
#     assert arrs.get([], 0, "test") == "test"


# def test_slice(array_fixture):
#     assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
#     assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
#     assert arrs.my_slice([]) == []
#     assert arrs.my_slice([1, 2, 3]) == [1, 2, 3]
