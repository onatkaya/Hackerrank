#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    word_list = list(map(str,s.split(' ')))

    new_list = []

    for a in word_list:
        new_list.append(a.capitalize())
    
    return (' '.join(new_list))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
