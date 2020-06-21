"""Tests for istanbul-setup.py.
"""
import random
istanbul_setup = __import__('istanbul-setup')

def test_islegal():
    random.seed(0)
    board = istanbul_setup.Board()
    board.islegal()

def test_main():
    istanbul_setup.main([])