# Enter your code here. Read input from STDIN. Print output to STDOUT
from fractions import Fraction as F
from decimal import Decimal as D
import statistics as st

n = int(input())
elements = input().split(" ")
elements = [ int(x) for x in elements ]

#mean 
mean = sum(elements)/len(elements)

#median
elements.sort()
if len(elements)% 2 == 0:
    median = float((elements[(len(elements)//2) - 1]) + (elements[(len(elements)//2)]) )/ 2
else:
    median = (elements[(len(elements)//2) + 1])

#mode
mode = max(set(elements), key=elements.count) 
ele_count = {}
for element in elements:
    ele_count[element] = elements.count(element)
values_with_maxocc = []
maxOcc = max(ele_count.values())
for element in elements:
    if ele_count[element] == maxOcc:
        values_with_maxocc.append(element)

if len(values_with_maxocc) == 1: mode = values_with_maxocc[0]
else: mode = min(values_with_maxocc)

print(mean)
print(median)
print(mode)
