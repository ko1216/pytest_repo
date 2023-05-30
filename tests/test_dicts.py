import pytest

from utils.dicts import get_val


@pytest.mark.parametrize('data, key, default, expected', [
    ({"word1": 6, 2: "word2"}, 2, "None", "word2"),
    ({"word1": 6, 2: "word2"}, 0, "empty", "empty"),
    ({}, 2, "None", "None"),
    ({"key1": "value1", "key2": "value2"}, "key2", "None", "value2")
])
def test_get_val(data: dict, key, default, expected):
    assert get_val(data, key, default) == expected
