#!/usr/bin/env python3
"""Generate Examples in README.
"""
import fileinput
import re

path = 'README.md'

def generate(path=path):
    # Read input.
    with open(path) as infile:
        contents = infile.read()

    # Regenerate examples.

    # Write output.
    with open(path, 'w') as outfile:
        outfile.write(contents)

if __name__ == '__main__':
    generate()