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
    places = shuffled(base_places)

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
        if legallayout(places):
            return places

def legallayout(places):
    count = len(places)
    width = math.isqrt(count)
    height = -(count // -width)
    col_max = width - 1
    row_max = height - 1

    # The Fountain (7) has to be one of the inner Places.
    fountain = divmod(places.index((7, 'Fountain')), width)
    if not (0 < fountain[0] < row_max and 0 < fountain[1] < col_max):
       return False

    # The Black Market (8) and the Tea House (9) must have a distance of at least
    # 3 Places from each other and must not be placed in the same column or row.
    black_market = divmod(places.index((8, 'Black Market')), width)
    tea_house = divmod(places.index((9, 'Tea House')), width)
    col_diff = abs(tea_house[1] - black_market[1])
    row_diff = abs(tea_house[0] - black_market[0])
    if col_diff + row_diff < 3 or col_diff < 1 or row_diff < 1:
        return False

    return True

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