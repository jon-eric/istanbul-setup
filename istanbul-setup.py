#!/usr/bin/env python3
"""Generate Istanbul board game setups.
"""

def main(args):
    for row in grouper(range(16), 4):
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