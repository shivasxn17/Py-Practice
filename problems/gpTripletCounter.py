#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countTriplets function below.
def countTriplets(arr, r):
    tripletCounter = 0
    n = len(arr) 
    for j in range(1, n - 1):       
        i = j - 1
        k = j + 1
  
        while (i >= 0 and k <= n - 1): 
            # if arr[j]/arr[i] = r and  
            # arr[k]/arr[j] = r and r  
            # is an integer (i, j, k) forms  
            # Geometric Progression 
            while (arr[j] / arr[i] == r and
                   arr[k] / arr[j] == r and
                   arr[j] // arr[i] == arr[k] // arr[j]): 
                
                tripletCounter += 1

                k += 1
                i += 1
   
            if(arr[j] / arr[i] == r and
                        arr[k] / arr[j] == r): 
              
                if(arr[j] // arr[i] < arr[k] // arr[j]): 
                    i -= 1
                else: 
                    k += 1

            elif (arr[j] % arr[i] == 0): 
                k += 1
            else: 
                i -= 1
    return tripletCounter*2    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
