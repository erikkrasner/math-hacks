#! /usr/bin/env python

# Prints n-digit Thue-Morse sequence in O(n log n) time.
#  http://en.wikipedia.org/wiki/Thue%E2%80%93Morse_sequence

import sys

def nth_thue_morse(n):
    num_ones = 0
    while n:
	num_ones += n & 1
	n >>= 1
    return num_ones % 2

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print ''.join(str(nth_thue_morse(n)) for n in xrange(int(sys.argv[1])))
