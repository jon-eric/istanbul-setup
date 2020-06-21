"""Tests for istanbul-setup.py.
"""
import functools
istanbul_setup = __import__('istanbul-setup')
Board = functools.partial(istanbul_setup.Board, shuffle=False)

def test_islegal():
    assert Board().islegal()
    assert not Board(mocha=True, letters=True).islegal()

def test_main():
    istanbul_setup.main([])