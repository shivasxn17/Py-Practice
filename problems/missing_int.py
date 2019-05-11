
def getSmallestMissingInt(A):
  a = set(A)
  b = set(range(1,len(A)+2))
  return min(b-a)

A = [1, 3, 6, 4, 1, 2]
print(getSmallestMissingInt(A))

A = [-1, -3]
print(getSmallestMissingInt(A))


