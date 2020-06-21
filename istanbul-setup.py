#!/usr/bin/env python3
"""Generate Istanbul board game setups.
"""
import argparse
import math
import random

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--mocha', help="Enable Mocha & Baksheesh", action='store_true')
parser.add_argument('--letters', help="Enable Letters & Seals", action='store_true')

def main(args):
    # Parse args.
    args = parser.parse_args(args)

    # Layout the board.
    board = Board(args.mocha, args.letters)

    # Print board.
    for line in board.render():
        print(line)

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

    letters_places = dict(enumerate([
        "Embassy",
        "Kiosk",
        "Auction House",
        "Secret Society"], 21))

    bazaar_places = dict(enumerate([
        "Catacombs"], 25))

    names = {**base_places, **mocha_places, **letters_places, **bazaar_places}

    def __init__(self, mocha=False, letters=False, shuffle=True):
        self.places = list(self.base_places)
        if mocha:
            self.places.extend(self.mocha_places)
        if letters:
            self.places.extend(self.letters_places)
        if mocha and letters:
            self.places.extend(self.bazaar_places)
        self.layout(shuffle)

    def islegal(self):
        """Return True if the board layout is legal.
        """
        # The Fountain (7) has to be one of the innermost Places.
        if self.find(7) not in self.inner:
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
        self.height = math.isqrt(count)
        self.width = count // self.height
        self.inner = self._inner(self.height, self.width)
        while shuffle:
            random.shuffle(self.places)
            if not legalonly or self.islegal():
                return self

    @staticmethod
    def _inner(height, width):
        """Return a set of (row, col) legal "inner" Fountain spaces.
        """
        border = min((height - 1) // 2, (width - 1) // 2)
        return {(row, col) for row in range(border, height - border)
                           for col in range(border, width  - border)}

    def render(self):
        """Render the board.
        """
        id_width = max(len(f'{id}') for id in self.places)
        names = [self.names[id] for id in self.places]
        name_width = max(len(name) for name in names)
        items = [f'{id:{id_width}}) {name:^{name_width}}' for id, name in zip(self.places, names)]
        yield from rendertable(grouper(items, self.width))

def rendertable(table):
    """Render a 2D table as an iterable of lines.
    """
    for i, row in enumerate(table):
        if i == 0:
            yield ''
            yield '+-' + '-+-'.join('-' * len(item) for item in row) + '-+'
        yield '| ' + ' | '.join(row) + ' |'
        yield '+-' + '-+-'.join('-' * len(item) for item in row) + '-+'

def grouper(iterable, n):
    """Collect data into fixed-length chunks or blocks.
    """
    # grouper('ABCDEFG', 3) --> ABC DEF"
    args = [iter(iterable)] * n
    return zip(*args)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
