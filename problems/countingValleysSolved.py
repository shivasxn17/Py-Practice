#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    valleys = 0
    steps = {}
    seaLvl = 0

    for step in range(n):
        if s[step] == 'U':
            seaLvl += 1
            if seaLvl == 0:
                valleys += 1
        else:
            seaLvl -= 1
    
    return(valleys)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    fptr.write(str(result) + '\n')
    fptr.close()
