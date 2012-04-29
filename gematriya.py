#! /usr/bin/python
# simple test to prove
#  http://www.youtube.com/watch?v=h60r2HPsiuM
#  is utter lunacy


from string import lowercase as alphabet
from collections import defaultdict
from operator import mul
import sys

def gematriya(word):
    global dictionary
    return sum(1 + alphabet.index(letter)
               for letter in word if letter in alphabet)

memo_table = {}

def count_all_gematriya():
    global dictionary, counts
    counts = defaultdict(int)
    for word in dictionary:
        g = gematriya(word)
        counts[g] = counts[g] + 1
    for g in counts:
        memo_table[g, 1] = counts[g]

def count_phrases_adding_up_to(total, num_words):
    if total == 0 or num_words == 0:
        return 0
    if (total, num_words) in memo_table:
        return memo_table[total, num_words]
    answer = sum(count_phrases_adding_up_to(subtotal, num_words - 1) *
                count_phrases_adding_up_to(total - subtotal, 1)
                  for subtotal in xrange(total + 1))
    memo_table[total,num_words] = answer
    return answer

if __name__ == '__main__':
    global dictionary
    dictionary = [line[:-1] for line in open('/usr/share/dict/words')]
    count_all_gematriya()
    print reduce(mul, (count_phrases_adding_up_to(n, 3) for n in (96,98,100,101)))
