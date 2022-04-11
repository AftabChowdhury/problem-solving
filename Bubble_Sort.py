def bubbleSort(array):
    # Best: O(n) time | O(1) space
    # Worst O(n^2) time | O(1) space
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                # array[j], array[j+1] = array[j+1], array[j]
    return array


print(bubbleSort([8, 5, 2, 9, 5, 6, 3]))
