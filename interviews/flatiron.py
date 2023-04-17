# write a t-9 calculator
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 't9_to_words' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING numbers
#  2. 2D_STRING_ARRAY key_map
# [[],[],["a","b",c"],"def",""]
# ["a", "b", "c"]
#  3. STRING_ARRAY valid_words
#

# numbers = "43556 ""= hello
def t9_to_words(numbers, key_map, valid_words):
    # initialize list of possible words
    curr_words = []
    new_words = []
    first_letter = True
    ret = []
    # loop through numbers
    for n in numbers:
        # for each number get letters
        # n = 3, pw = [g,h,i]
        letters = key_map[int(n)]
        # ls = [d,e,f]
        # fl = False
        if first_letter:
            # g h i 
            for l in letters:
                curr_words.append(l)
                # pw = [g,h,i]
            first_letter = False
            print(curr_words)
        else:
            for w in curr_words:
                # cw = [g,h,i]
                # w = g
                for l in letters:
                    # add letters to each word in existing list of possible valid words
                    # hd, he, hf
                    new_words.append(w + l)
            curr_words = new_words
            new_words = []
            print(new_words)
        # [gdjjm,ge,gf,hd,he...]
    
    # check/lookup possible words against valid_words
    for pw in curr_words:
        for v in valid_words:
            if pw == v:
                ret.append(pw)
    
    # return only words that are valid
    print(ret)
    return ret

# 43556 = hello
# 4 --> g h i
# 3 --> gd ge gf hd he...
# 5 --> gdj gdk gdl gej gek gel
# hm[g] = [d,e,f]

if __name__ == '__main__':  
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    numbers = input()

    key_map_rows = int(input().strip())
    key_map_columns = int(input().strip())

    key_map = []

    for _ in range(key_map_rows):
        key_map.append(input().rstrip().split())

    valid_words_count = int(input().strip())

    valid_words = []

    for _ in range(valid_words_count):
        valid_words_item = input()
        valid_words.append(valid_words_item)

    result = t9_to_words(numbers, key_map, valid_words)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()