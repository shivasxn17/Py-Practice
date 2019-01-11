#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    minJumps = []
    for i in range(len(c)):
        if(i == 0 and c[i] == 0):
            minJumps.append(i)
        elif(c[i] == 0):
            minJumps.append(i)
            if i-2 in minJumps:
                if i-1 in minJumps: minJumps.remove(i-1)
    print(minJumps)
    return len(minJumps) - 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    fptr.write(str(result) + '\n')
    fptr.close()
