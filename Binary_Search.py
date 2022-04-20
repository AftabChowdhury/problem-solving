def binarySearch(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = int((left + right) / 2)
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            right = mid - 1
            mid = right
        elif target > array[mid]:
            left = mid + 1
            mid = left
    return -1


print(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33))
