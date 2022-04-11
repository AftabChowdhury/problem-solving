# Best: O(n) time | O(1) space
# Worst O(n^2) time | O(1) space
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key
    return array


print(insertionSort([8, 5, 2, 9, 5, 6, 3]))
