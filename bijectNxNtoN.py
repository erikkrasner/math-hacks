#! /usr/bin/python

#Illustrates a neat bijection between
# NxN and N.

import sys

def pi(x,y):
    return (2**x * (2*y + 1)) -1

def pi_one_and_two(p):
    p += 1
    pi_one = 0
    power = 1
    while p % (power * 2) == 0:
        pi_one += 1
        power *= 2
    pi_two = (p / power - 1) / 2
    return pi_one, pi_two

def all_pairs_summing_up_to(n):
    for xPlusY in xrange(n+1):
	for y in xrange(xPlusY+1):
            yield pi(xPlusY - y, y)

def all_unpairs_up_to(n):
    return (pi_one_and_two(i) for i in xrange(n))

def print_pairs_summing_up_to(n):
    print "\n".join(str(pi) for pi in all_pairs_summing_up_to(n))

def print_unpairs_up_to(n):
    print "\n".join(str(pi1) + " " + str(pi2)
                    for pi1, pi2 in all_unpairs_up_to(n))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if len(sys.argv) > 2 and sys.argv[2] == "-u":
            print_unpairs_up_to(int(sys.argv[1]))
        else:
            print_pairs_summing_up_to(int(sys.argv[1]))
    else:
        print "first ten pairings:"
        print_pairs_summing_up_to(10)
        print "first ten unpairings:"
        print_unpairs_up_to(10)
