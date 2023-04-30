import pytest
from hash_tables.hash_tables import get_missing_numbers_in_range

def test_get_missing_numbers_in_range():
    assert get_missing_numbers_in_range([10, 12, 11, 15], 10, 15) == [13, 14]


def test_get_missing_numbers_in_range_small_range():
    assert get_missing_numbers_in_range(
        [1, 14, 11, 51, 15], 50, 55) == [50, 52, 53, 54]