#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    pairCount = 0 
    temp = {}
    
    for sock in ar:
        if sock not in temp.keys(): 
            temp[sock] = 1
        else: 
            pairCount += 1
            del temp[sock]

    return pairCount
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
