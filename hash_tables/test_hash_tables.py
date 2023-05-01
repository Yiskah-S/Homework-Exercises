import pytest
from hash_tables.hash_tables import get_missing_numbers_in_range, get_symmetric_pairs, get_intersection, is_permutation, is_palindrome_permutation

def test_get_missing_numbers_in_range():
    assert get_missing_numbers_in_range([10, 12, 11, 15], 10, 15) == [13, 14]


def test_get_missing_numbers_in_range_small_range():
    assert get_missing_numbers_in_range(
        [1, 14, 11, 51, 15], 50, 55) == [50, 52, 53, 54]
    
def test_get_symmetric_pairs():
    pairs = [[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]]
    assert get_symmetric_pairs(pairs) == [[30, 40], [5, 10]]


def test_get_symmetric_pairs_strings():
    pairs = [["Dan", "Kari"], ["Jeremy", "Val"], ["Jeremy", "Charles"], [
        "Devin", "Susan"], ["Kari", "Dan"], ["Devin", "Susan"]]
    assert get_symmetric_pairs(pairs) == [["Dan", "Kari"]]


def test_get_symmetric_pairs_no_pairs():
    pairs = [["Dan", "Kari"], ["Lisa", "Val"], ["Jeremy", "Charles"],
            ["Devin", "Susan"], ["Charles", "Jamie"]]
    assert get_symmetric_pairs(pairs) == []

def test_get_intersection_one_match():
    red = [2, 3, 4]
    blue = [4, 5, 6]
    assert get_intersection(red, blue) == [4]


def test_get_intersection_no_matches():
    red = [9, 30, 42]
    blue = [56, 34, 90, 32]
    assert get_intersection(red, blue) == []


def test_get_intersection_many_matches():
    red = [50, 43, 25, 72]
    blue = [25, 36, 43, 50, 80]
    result = get_intersection(red, blue)
    assert 25 in result
    assert 43 in result
    assert 50 in result
    assert len(result) == 3

def test_is_permutation():
    assert is_permutation("hello", "ehllo")

def test_is_permutation_false_different_qty_letters():
    assert not is_permutation("heelo", "ehllo")

def test_is_permutation_false_different_letters():
    assert not is_permutation("pizza", "pasta")

def test_is_permutation_unmatching_lengths():
    assert not is_permutation("pizza", "piza")

def test_is_permutation_same_word():
    assert is_permutation("pizza", "pizza")

def test_is_permutation_empty_strings():
    assert is_permutation("", "")

def test_is_palindrome_permutation_simple():
    assert is_palindrome_permutation("lool")

def test_is_palindrome_permutation_palindrome():
    assert is_palindrome_permutation("racecar")

def test_is_palindrome_permutation_rearranged_palindrome():
    assert is_palindrome_permutation("carrace")

def test_is_palindrome_permutation_incomplete():
    assert not is_palindrome_permutation("raceca")

def test_is_palindrome_permutation_unmatching_letters():
    assert not is_palindrome_permutation("hello")

def test_is_palindrome_permutation_empty_string():
    assert is_palindrome_permutation("")