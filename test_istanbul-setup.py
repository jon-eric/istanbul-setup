"""Tests for istanbul-setup.py.
"""
import functools
istanbul_setup = __import__('istanbul-setup')
Board = functools.partial(istanbul_setup.Board, shuffle=False)

def test_inner():
    assert len(Board().inner) == 4
    assert len(Board(mocha=True).inner) == 6
    assert len(Board(letters=True).inner) == 6
    assert len(Board(mocha=True, letters=True).inner) == 1

def test_islegal():
    assert Board().islegal(), "Unshuffled should be legal."
    assert not Board(mocha=True).islegal(), "Unshuffled plus one expansion isn't legal due to tea house."
    assert not Board(mocha=True, letters=True).islegal(), "Unshuffled Bazaar isn't legal due to fountain and tea house."

def test_main():
    istanbul_setup.main([])