import builtins
from unittest import mock
import pytest

from ai_tutor import Tutor


def test_invalid_category():
    with pytest.raises(ValueError):
        Tutor("invalid")


def test_scoring_all_correct():
    answers = ["4", "4", "5"]
    with mock.patch.object(builtins, "input", side_effect=answers):
        tutor = Tutor("math")
        with mock.patch.object(builtins, "print"):
            tutor.ask()
    assert tutor.correct == len(answers)

