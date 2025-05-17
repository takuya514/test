import builtins
import types
import pytest

import ai_tutor


def test_unknown_category():
    with pytest.raises(ValueError):
        ai_tutor.Tutor('unknown')


def test_all_correct(monkeypatch):
    tutor = ai_tutor.Tutor('math')
    answers = [q['answer'] for q in tutor.questions]
    inputs = iter(answers)
    monkeypatch.setattr(builtins, 'input', lambda _: next(inputs))
    tutor.ask()
    assert tutor.correct == tutor.total
