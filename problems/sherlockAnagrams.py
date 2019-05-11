#!/bin/python3

import math
import os
import random
import re
import sys
from collections import *

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(queryStr):
    check = defaultdict(int)

    lenQueryStr = len(queryStr)

    for i in range(lenQueryStr):
        for j in range(i+1, lenQueryStr+1):
            subStr = list(queryStr[i:j])
            subStr.sort()
            subStr = "".join(subStr)
            check[subStr]+=1

    sum = 0
    for i in check:
        n = check[i]
        sum += (n*(n-1))/2
        
    return int(sum)   

if __name__ == '__main__':
    q = 2
    s = ['abba','abcd']
    for word in s:
        result = sherlockAndAnagrams(word)
        print(str(result))
