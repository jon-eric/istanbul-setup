"""Tests for istanbul-setup.py.
"""
import functools
istanbul_setup = __import__('istanbul-setup')
Board = functools.partial(istanbul_setup.Board, shuffle=False)

def test_inner():
    assert len(Board().inner)                         == 4, "A 4x4 Base board should have 4 Fountain spaces."
    assert len(Board(mocha=True).inner)               == 6, "A 5x4 Mocha board should have 6 Fountain spaces."
    assert len(Board(letters=True).inner)             == 6, "A 5x4 Letters board should have 6 Fountain spaces."
    assert len(Board(mocha=True, letters=True).inner) == 1, "A 5x5 Bazaar board should have 1 Fountain space."

def test_islegal():
    assert Board().islegal(),                             "Unshuffled Base board should be legal."
    assert not Board(mocha=True).islegal(),               "Unshuffled Mocha board shouldn't be legal due to tea house."
    assert not Board(letters=True).islegal(),             "Unshuffled Letters board shouldn't be legal due to tea house."
    assert not Board(mocha=True, letters=True).islegal(), "Unshuffled Bazaar board shouldn't be legal due to fountain and tea house."

def test_main():
    istanbul_setup.main([])