def binary_search_recursive(listOfInts, elem, start=0, end=None):
    if end is None:
        end = len(listOfInts) - 1
    if start > end:
        return 'Value not found in list'

    mid = (start + end) // 2
    if elem == listOfInts[mid]:
        return mid
    if elem < listOfInts[mid]:
        return binary_search_recursive(listOfInts, elem, start, mid-1)
    # elem > listOfInts[mid]
    return binary_search_recursive(listOfInts, elem, mid+1, end)

listOfInts = [0,1,2,3,4,5,22,33,45]

print (binary_search_recursive(listOfInts, 22))
