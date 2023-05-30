import pytest

from utils.dicts import get_val


@pytest.mark.parametrize('data, key, default', [
    ({"word1": 6, 2: "word2"}, 2, "word2"),
    ({"word1": 6, 2: "word2"}, 0, "empty"),
    ({}, 2, "None"),
    ({"key1": "value1", "key2": "value2"}, "key2", "value2")
])
def test_get_val(data: dict, key, default):
    assert get_val(data, key, default)
