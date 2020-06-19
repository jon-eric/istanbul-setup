#!/usr/bin/env python3
"""Generate Istanbul board game setups.
"""
import math
import random

base_places = list(enumerate([
    "Wainwright",
    "Fabric Warehouse",
    "Spice Warehouse",
    "Fruit Warehouse",
    "Post Office",
    "Caravansary",
    "Fountain",
    "Black Market",
    "Tea House",
    "Large Market",
    "Small Market",
    "Police Station",
    "Sultan's Palace",
    "Small Mosque",
    "Great Mosque",
    "Gemstone Dealer"], 1))

def main(args):
    # Shuffle places.
    places = list(base_places)
    shuffled(places)

    # Print board.
    for line in genboard(places):
        print(line)

def genboard(places):
    """Generate board lines from a list of (idx, name) places.
    """
    count = len(places)
    width = math.isqrt(count)
    idx_width = max(len(str(idx)) for idx, name in places)
    name_width = max(len(name) for idx, name in places)
    items = [f'{idx:{idx_width}}) {name:^{name_width}}' for idx, name in places]
    yield ''
    for row in grouper(items, width):
        yield ' | '.join(row)

def shuffled(places):
    places = list(places)
    while True:
        random.shuffle(places)
        return places

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