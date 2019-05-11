#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
# def checkMagazine(magazine, note):
#     for word in note:
#         if word in magazine:
#             magazine.remove(word)
#         else:
#             return "No"
#     return "Yes"

from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    if (Counter(note) - Counter(magazine)) == {}: 
        return "Yes"
    return "No"

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    if m >= n:
        print(checkMagazine(magazine, note))
    else:
        print("No")
