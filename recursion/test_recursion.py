import pytest
from recursion.recursion import 

def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_positive_num():
    assert factorial(5) == 5 * 4 * 3 * 2 * 1


def test_factorial_negative_num():
    with pytest.raises(ValueError):
        factorial(-1)

def test_reverse_word():
    assert reverse("cat") == "tac"


def test_reverse_single_character():
    assert reverse("a") == "a"


def test_reverse_empty_string():
    assert reverse("") == ""

def test_bunny_zero_bunnies():
    assert bunny(0) == 0


def test_bunny_one_bunny_has_two_ears():
    assert bunny(1) == 2


def test_bunny_fifty_bunnies_have_100_ears():
    assert bunny(50) == 100

def test_is_nested_parens():
    parens = "((()))"

    assert is_nested_parens(parens)


def test_is_nested_parens_empty_str():
    assert is_nested_parens("")


def test_is_nested_parens_not_matching_length():
    parens = "(())))"

    assert not is_nested_parens(parens)

def test_search_success_unsorted():
    assert search(["b", "c", "a"], "a")


def test_search_empty_array():
    assert not search([], "a")


def test_search_success_first_item():
    assert search(["a", "b", "c"], "a")


def test_search_not_found():
    assert not search(["a", "b", "c"], "🌈")

def test_is_palindrome_success():
    assert is_palindrome("racecar")


def test_is_palindrome_not_palindrome():
    assert not is_palindrome("raecar")

def test_digit_match_large_inputs():
    apples = 1072503891
    oranges = 62530841

    assert digit_match(apples, oranges) == 4


def test_digit_match_no_matches():
    apples = 0
    oranges = 62530841

    assert digit_match(apples, oranges) == 0


def test_digit_match_clustered_matches():
    apples = 841
    oranges = 62530841

    assert digit_match(apples, oranges) == 3


def test_digit_match_single_digits():
    apples = 0
    oranges = 0

    assert digit_match(apples, oranges) == 1


def test_digit_match_small_inputs():
    apples = 10
    oranges = 20

    assert digit_match(apples, oranges) == 1