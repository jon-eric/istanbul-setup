#!/usr/bin/env python3
"""Generate Examples in README.
"""
import fileinput
import re

path = 'README.md'

headerpat = re.compile(r'Examples?\n-+')

def generate(path=path):
    # Read input.
    with open(path) as infile:
        contents = infile.read()

    # Regenerate examples.
    contents = headerpat.sub('\n'.join(examplelines()), contents)

    # Write output.
    with open(path, 'w') as outfile:
        outfile.write(contents)

def examplelines():
    yield mdheader('Example')

def mdheader(name):
    return name + '\n' + '-' * len(name)

if __name__ == '__main__':
    generate()