def weightedMean(n,elementsArr,weightsArr):
    prodSum = 0.0
    for i in range(n):
        prodSum += elementsArr[i] * weightsArr[i]
    return round(prodSum/sum(weightsArr),1)

n = int(input())

elementsArr = input().split(" ")
elementsArr = list(map(float, elementsArr))

weightsArr = input().split(" ")
weightsArr = list(map(float, weightsArr))

print(weightedMean(n,elementsArr,weightsArr))