#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    s_count = s.count('a')
    if n%len(s) == 0:
        return s_count*(n//len(s))
    else:
        temp_a = s[0:n%len(s)].count('a')
        return s_count*(n//len(s)) + temp_a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    fptr.write(str(result) + '\n')
    fptr.close()
