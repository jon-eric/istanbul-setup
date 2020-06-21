#!/usr/bin/env python3
"""Generate Examples in README.
"""
import io
import random
import re
from contextlib import redirect_stdout
istanbul_setup = __import__('istanbul-setup')

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
    # Example input.
    yield ''
    yield ' '.join(['$ istanbul-setup.py'] + args)

    # Example output.
    with io.StringIO() as f:
        with redirect_stdout(f):
            istanbul_setup.main(args)
        f.seek(0)
        yield from f

def mdheader(name):
    return name + '\n' + '-' * len(name)

def mdcode(lines):
    yield from (f'    {line}'.rstrip() for line in lines)

if __name__ == '__main__':
    generate()
