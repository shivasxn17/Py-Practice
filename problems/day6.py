# Enter your code here. Read input from STDIN. Print output to STDOUT
#!/bin/python3
import math
import os
import random
import re
import sys


def evenOdd(str):
    evenArr = []
    oddArr = []

    for i in range(len(str)):
        if i%2 == 0: evenArr.append(str[i])
        else: oddArr.append(str[i])

    return ''.join(evenArr) + ' ' + ''.join(oddArr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    
    for i in range(n):
        str = input()
        fptr.write(evenOdd(str) + '\n')

    fptr.close()