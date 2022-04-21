# O(n) time | O(1) space
def max_subset_sum_no_adjacent(array):
    # Write your code here.
    if len(array) < 1:
        return 0
    if len(array) == 1:
        return array[0]
    if len(array) == 2:
        return max(array[0], array[1])
    exclusive_sum = array[0]
    inclusive_sum = max(array[0], array[1])
    for i in range(2, len(array)):
        temp = inclusive_sum
        inclusive_sum = max(inclusive_sum, exclusive_sum + array[i])
        exclusive_sum = temp
    return inclusive_sum


print(max_subset_sum_no_adjacent([75, 105, 120, 75, 90, 135]))
# print(maxSubsetSumNoAdjacent([75, 105]))
