#! /usr/bin/python

#Illustrates a neat bijection between
# NxN and N.

import sys

def all_pairs_summing_up_to(n):
    for xPlusY in range(n+1):
	for y in range(xPlusY+1):
            yield pi(xPlusY - y, y)

def pi(x,y):
    return (2**x * (2*y + 1)) -1

def print_pairs_summing_up_to(n):
    for pi in all_pairs_summing_up_to(n):
	print pi

if __name__ == '__main__':
    if len(sys.argv) > 1:
        print_pairs_summing_up_to(int(sys.argv[1]))
    else:
        print_pairs_summing_up_to(10)
