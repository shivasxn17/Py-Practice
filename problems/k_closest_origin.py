"""
Amazon Fresh

Amazon Fresh is a grocery delivery service that offers consumers the option of purchasing 
their groceries online and schedule future deliveries of purchased groceries. 
Amazon's backend system dynamically tracks each Amazon Fresh delivery truck and 
automatically assigns the next deliveries in a truck's plan. To accomplish this, 
the system generates an optimized delivery plan with X destinations. The most optimized plan would
deliver to the closest X destinations from the start among all of the possible destinations in the plan. 

 Given an array of N possible delivery destinations, 
 	implement an algorithm to create the delivery plan for the closest X destinations.

Input
The input to the function/method consists of three arguments:
	numDestinations, 
		an integer representing the total number of possible delivery destinations for the truck (N);
	allLocations, 
		a list where each element consists of a pair of integers representing the x and y coordinates of the delivery locations; from aonecode.com
	numDeliveries, 
		an integer representing the number of deliveries that will be delivered in the plan (X).

Output from aonecode.com
	Return a list of elements where each element of the list represents the x and y integer coordinates of the delivery destinations.from aonecode.com

Constraints
	numDeliveries <= numDestinations from aonecode.com

Input:
	numDestinations = 3 
	allocations = [[1, 2], [3, 4], [1, -1]]
	numDeliveries = 2 from a

output

 [[1, -1], [1, 2]]

"""
from math import sqrt
from operator import itemgetter

def calcDistances(allocations):
	locWithDist = {}
	for loc in allocations:
		x,y = loc
		dist = sqrt(x**2 + y**2) 
		locWithDist[tuple(loc)] = dist
	return locWithDist

def closestDeliveries(allocations, numDeliveries): 
	# allocations.sort(key = lambda numDeliveries: numDeliveries[0]**2 + numDeliveries[1]**2) 
	locWithDist = calcDistances(allocations)
	sortedDist = sorted(locWithDist.items(),key=itemgetter(1),reverse = False)
	closestDeliveries = sortedDist[0:numDeliveries]

	output = []
	for delivery in closestDeliveries:
		output.append(list(delivery[0]))

	# return allocations[:numDeliveries] 
	return output

if __name__ == '__main__':
	# numDestinations = int(input())
	# allocations = input()
	# numDeliveries = int(input())
	allocations = [[1, 2], [3, 4], [1, -1]]
	numDeliveries = 2
	  
	print(closestDeliveries(allocations, numDeliveries)) 