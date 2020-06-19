#!/usr/bin/env python3
"""Generate Istanbul board game setups.
"""
import math

tiles = list(range(16))

def main(args):
    print_board(tiles)

def print_board(tiles):
    """Print an iterable of tile indexes.
    """
    print()
    count = len(tiles)
    width = math.isqrt(count)
    for row in grouper(tiles, width):
        print(' | '.join(str(idx) for idx in row))

def grouper(iterable, n):
    """Collect data into fixed-length chunks or blocks.
    """
    # grouper('ABCDEFG', 3) --> ABC DEF"
    args = [iter(iterable)] * n
    return zip(*args)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

def test_main():
    main([])