
import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))

numSwaps = 0
firstElement = 0 
lastElement = 0 

for i in range(n):
	iterSwap = 0
	for j in range(n-1):
		if (a[j] > a[j+1]):
			a[j],a[j+1] = a[j+1],a[j]
			iterSwap += 1
	numSwaps += iterSwap
	if(iterSwap == 0): break

print("Array is sorted in {} swaps.".format(numSwaps))
print("First Element: {}".format(a[0]))
print("Last Element: {}".format(a[-1]))

