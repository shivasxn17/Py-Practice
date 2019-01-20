from math import sqrt

def calcStdDeviation(n,distribution):
    distMean = sum(distribution)/n
    distSum = 0.0
    for element in distribution:
        distSum += (element - distMean)**2
    return round((sqrt(distSum/n)),1)

n = int(input())    
distribution = list(map(float,(input().split(" "))))
print(calcStdDeviation(n,distribution))