import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from logic_utils import check_guess, parse_guess, update_score


def test_winning_guess():
    # FIX: secret stays as integer, never string
    result, message = check_guess(50, 50)
    assert result == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be Too High
    result, message = check_guess(60, 50)
    assert result == "Too High"


def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be Too Low
    result, message = check_guess(40, 50)
    assert result == "Too Low"


def test_parse_guess_valid():
    ok, value, err = parse_guess("42")
    assert ok == True
    assert value == 42


def test_parse_guess_empty():
    ok, value, err = parse_guess("")
    assert ok == False


def test_score_decreases_on_wrong_guess():
    # FIX: wrong guesses should never increase score
    result = update_score(100, "Too High", 2)
    assert result == 95
