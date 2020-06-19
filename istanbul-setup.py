#!/usr/bin/env python3
"""Generate Istanbul board game setups.
"""
import math

tiles = list(range(16))

base_places = ['Wainwright',
               'Fabric Warehouse',
               'Spice Warehouse',
               'Fruit Warehouse']

def main(args):
    print_board(base_places)

def print_board(names):
    """Print an iterable of tile names.
    """
    count = len(names)
    width = math.isqrt(count)
    name_width = max(len(name) for name in names)
    items = [f'{idx+1}. {name:{name_width}}' for idx, name in enumerate(names)]
    print()
    for row in grouper(items, width):
        print(' | '.join(row))

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