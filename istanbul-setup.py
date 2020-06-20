#!/usr/bin/env python3
"""Generate Istanbul board game setups.
"""
import math
import random

class Board:
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
    fountain = base_places[6]
    tea_house = base_places[8]
    black_market = base_places[9]

    def __init__(self, places=base_places):
        self.places = list(places)
        count = len(self.places)
        self.width = math.isqrt(count)
        self.height = -(count // -self.width)
        self.max = self.height - 1, self.width - 1

    def islegal(self):
        # The Fountain (7) has to be one of the inner Places.
        fountain = self.find(self.fountain)
        if not (0 < fountain[0] < self.max[0] and 0 < fountain[1] < self.max[0]):
            return False

        # The Black Market (8) and the Tea House (9) must have a distance of at least
        # 3 Places from each other and must not be placed in the same column or row.
        black_market = self.find(self.black_market)
        tea_house = self.find(self.tea_house)
        col_diff = abs(tea_house[1] - black_market[1])
        row_diff = abs(tea_house[0] - black_market[0])
        if col_diff + row_diff < 3 or col_diff < 1 or row_diff < 1:
            return False

        return True

    def find(self, place):
        return divmod(self.places.index(place), self.width)

    def render(self):
        idx_width = max(len(str(idx)) for idx, name in self.places)
        name_width = max(len(name) for idx, name in self.places)
        items = [f'{idx:{idx_width}}) {name:^{name_width}}' for idx, name in self.places]
        yield ''
        for row in grouper(items, self.width):
            yield ' | '.join(row)

    def shuffle(self):
        while True:
            random.shuffle(self.places)
            if self.islegal():
                return self

def main(args):
    # Shuffle places.
    board = Board()
    board.shuffle()

    # Print board.
    for line in board.render():
        print(line)

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