def bs(collection, value):
    left, right = 0, len(collection) - 1
    while left <= right:
        mid = (left + right) // 2
        if collection[mid] < value:
            left = mid + 1
        elif value < collection[mid]:
            right = mid - 1
        else:
            return mid
    return None

sample = [0,2,3,7,8]
print(bs(sample, 7))