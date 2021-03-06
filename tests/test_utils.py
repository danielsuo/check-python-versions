import sys
from io import StringIO

from check_python_versions.utils import pipe, confirm


def test_pipe():
    assert pipe('echo', 'hi') == 'hi\n'


def test_confirm_eof(monkeypatch):
    monkeypatch.setattr(sys, 'stdin', StringIO())
    assert not confirm("Hello how are you?")


def test_confirm_default(monkeypatch):
    monkeypatch.setattr(sys, 'stdin', StringIO("\n"))
    assert not confirm("Hello how are you?")


def test_confirm_no(monkeypatch):
    monkeypatch.setattr(sys, 'stdin', StringIO("n\n"))
    assert not confirm("Hello how are you?")


def test_confirm_yes(monkeypatch):
    monkeypatch.setattr(sys, 'stdin', StringIO("y\n"))
    assert confirm("Hello how are you?")


def test_confirm_neither(monkeypatch):
    monkeypatch.setattr(sys, 'stdin', StringIO("t\ny\n"))
    assert confirm("Hello how are you?")
