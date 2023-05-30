import pytest

from utils import arrs


@pytest.mark.parametrize('array, index, default', [
    ([1, 2, 3], 1, 2),
    ([1, 2, 3], -1, "test")
])
def test_get(array, index, default):
    assert arrs.get(array, index, default)


def test_get__index_error():
    with pytest.raises(IndexError):
        arrs.get([], 0, "test")


@pytest.mark.parametrize('coll, start, end, expected', [
    ([1, 2, 3, 4], 1, 3, [2, 3]),
    ([1, 2, 3], 1, None, [2, 3]),
    ([1, 2, 3], -2, None, [2, 3]),
    ([1, 2, 3], -3, -2, [1]),
    ([], 0, None, []),
    ([1], -3, 0, [])
])
def test_my_slice(coll: list, start, end, expected: list):
    assert arrs.my_slice(coll, start, end) == expected
