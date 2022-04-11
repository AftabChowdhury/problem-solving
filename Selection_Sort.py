# Best: O(n) time | O(1) space
# Worst O(n^2) time | O(1) space
def selectionSort(array):
    for i in range(len(array)):
        min_value_index = i
        for j in range(i+1, len(array)):
            if array[min_value_index] > array[j]:
                min_value_index = j
        array[i], array[min_value_index] = array[min_value_index], array[i]
    return array


print(selectionSort([8, 5, 2, 9, 5, 6, 3]))
