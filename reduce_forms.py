#!/usr/bin/python

#for reducing binary quadratic forms
#works with examples from class
#takes some liberties with what b is

def reduce_form(a,b,c):
    while True:
    	print a,b,c
	if c < a:
	    print "s"
            a, b, c = c, -b, a
	elif 2 * abs(b) >= abs(a):
	    k = (a - 2*b) / (2 * a)
	    print "t", k
	    a, b, c = a, k*a + b, k*k*a + 2*k*b + c
	else:
	    return a,2*b,c
