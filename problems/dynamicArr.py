#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the dynamicArray function below.
def dynamicArray(n, queries):
    seqList = []
    lastAnswer = 0
    print(queries)
    for i in range(len(queries)):
        if queries[i] == 2:
            lastAnswer = (queries[i][0] ^ lastAnswer) % n
            print(lastAnswer)



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nq = input().rstrip().split()
    n = int(nq[0])
    q = int(nq[1])
    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()