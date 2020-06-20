#!/usr/bin/env python3
"""Generate Istanbul board game setups.
"""
import math
import random

class Board:
    base_places = dict(enumerate([
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

    mocha_places = dict(enumerate([
        "Roasting Plant",
        "Guild Hall",
        "Tavern",
        "Coffee House"], 17))

    names = {**base_places, **mocha_places}

    def __init__(self, mocha=False, shuffle=True):
        self.places = list(self.base_places)
        if mocha:
            self.places.extend(self.mocha_places)
        self.layout(shuffle)

    def islegal(self):
        """Return True if the board layout is legal.
        """
        # The Fountain (7) has to be one of the inner Places.
        fountain = self.find(7)
        if not (0 < fountain[0] < self.max[0] and 0 < fountain[1] < self.max[1]):
            return False

        # The Black Market (8) and the Tea House (9) must have a distance of at least
        # 3 Places from each other and must not be placed in the same column or row.
        black_market = self.find(8)
        tea_house = self.find(9)
        col_diff = abs(tea_house[1] - black_market[1])
        row_diff = abs(tea_house[0] - black_market[0])
        if col_diff + row_diff < 3 or col_diff < 1 or row_diff < 1:
            return False

        return True

    def find(self, place):
        """Return (row, column) of place.
        """
        return divmod(self.places.index(place), self.width)

    def layout(self, shuffle=True, legalonly=True):
        """Layout the board.
        """
        count = len(self.places)
        height = math.isqrt(count)
        self.width = count // height
        self.max = height - 1, self.width - 1
        while shuffle:
            random.shuffle(self.places)
            if not legalonly or self.islegal():
                return self

    def render(self):
        """Render the board.
        """
        id_width = max(len(f'{id}') for id in self.places)
        names = [self.names[id] for id in self.places]
        name_width = max(len(name) for name in names)
        items = [f'{id:{id_width}}) {name:^{name_width}}' for id, name in zip(self.places, names)]
        yield ''
        for row in grouper(items, self.width):
            yield ' | '.join(row)

def grouper(iterable, n):
    """Collect data into fixed-length chunks or blocks.
    """
    # grouper('ABCDEFG', 3) --> ABC DEF"
    args = [iter(iterable)] * n
    return zip(*args)

def main(args):
    # Layout the board.
    board = Board()

    # Print board.
    for line in board.render():
        print(line)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])

def test_main():
    main([])