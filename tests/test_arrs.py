import pytest

from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([1, 2, 3], -1, "test") == "test"


def test_get__index_error():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


def test_my_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -2) == [2, 3]
    assert arrs.my_slice([1, 2, 3], -3, -2) == [1]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice([1], -3, 0) == []
