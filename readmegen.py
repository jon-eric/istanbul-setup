#!/usr/bin/env python3
"""Generate Examples in README.
"""
import fileinput
import random
import re
module = __import__('istanbul-setup')

path = 'README.md'

examples = [[]]

pattern = re.compile(r'Examples?\n-+\n.+$', re.DOTALL)

def generate(path=path, examples=examples):
    # Read input.
    with open(path) as infile:
        contents = infile.read()

    # Regenerate examples.
    random.seed(0)
    examples = '\n'.join(exampleslines(examples))
    contents = pattern.sub(examples, contents)

    # Write output.
    with open(path, 'w') as outfile:
        outfile.write(contents)

def exampleslines(examples):
    yield mdheader('Examples' if len(examples) > 1 else 'Example')
    for args in examples:
        yield from mdcode(examplelines(args))

def examplelines(args):
    # Shuffle places.
    places = list(module.base_places)
    random.shuffle(places)

    # Example input.
    yield ''
    yield ' '.join(['$ istanbul-setup.py'] + args)

    # Example output.
    yield ''
    yield from module.genboard(places)

def mdheader(name):
    return name + '\n' + '-' * len(name)

def mdcode(lines):
    yield from (f'    {line}'.rstrip() for line in lines)

if __name__ == '__main__':
    generate()
