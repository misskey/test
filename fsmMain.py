from __future__ import generators

import json
import sys

# Jump targets not state-sensitive, only to simplify example
from glob import glob
from macpath import dirname, abspath, join

from parser import Parser
from reader import Reader


def jump_to(val):
    if 0 <= val < 10:
        return 'ONES'
    else:
        return 'OUT_OF_RANGE'



def scheduler(gendct, start):
    global cargo
    coroutine = start
    while 1:
        (coroutine, cargo) = gendct[coroutine].next()


def math_gen(n):  # Iterative function becomes a generator
    from math import sin
    while 1:
        yield n
        n = abs(sin(n)) * 31


def get_ones(iter):
    global cargo
    while 1:
        print "\nONES State:   ",
        while jump_to(cargo) == 'ONES':
            print "@ %2.1f " % cargo,
            cargo = iter.next()
        yield (jump_to(cargo), cargo)

def get_tens(iter):
    global cargo
    while 1:
        print "\nTENS State:   ",
        while jump_to(cargo) == 'TENS':
            print "#%2.1f " % cargo,
            cargo = iter.next()
        yield (jump_to(cargo), cargo)
def exit(iter):
    jump = raw_input('\n\n[co-routine for jump?] ').upper()
    print "...Jumping into middle of", jump
    yield (jump, iter.next())
    print "\nExiting from exit()..."
    sys.exit()

def toJSON(input):
      reader = Reader(input)
      parser = Parser(reader, asJson=True)
      return json.dumps(parser.runtime)

    #     num_stream = math_gen(1)
    #     cargo = num_stream.next()
    # gendct = {'ONES': get_ones(num_stream),'TENS': get_tens(num_stream), 'OUT_OF_RANGE': exit(num_stream)}
    # scheduler(gendct, jump_to(cargo))
if __name__ == "__main__":
    DIR = dirname(abspath(__file__))
    TOMLFiles = glob(join(DIR, '*.toml'))
    if __name__ == '__main__':
        for filename in TOMLFiles:
            with open(filename) as file:
                print  toJSON(file)