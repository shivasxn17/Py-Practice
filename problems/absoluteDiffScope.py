class Difference:
    def __init__(self, a):
        self.__elements = a
	
	maximumDifference = None
	def computeDifference(self):
		maxE = max(self.__elements)
		minE = min(self.__elements)
		maximumDifference = abs((abs(maxE) - abs(minE))

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)