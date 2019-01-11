#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    output = open(os.environ['OUTPUT_PATH'],'w')
    n = int(input())
    stack = []
    while n != 0:
        if n%2 == 0:
            stack.append('0')
        else: 
            stack.append('1')
        n = n //2
    stack.reverse()
    stack = "".join(stack)
    output.write(str((max(len(s) for s in re.findall(r'1+', "".join(stack))))))