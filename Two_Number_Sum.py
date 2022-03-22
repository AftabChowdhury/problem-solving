def two_number_sum_bfm(array, targetSum):
    result = []
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            sum = array[i] + array[j]
            if sum == targetSum:
                result.append(array[i])
                result.append(array[j])
    return result


print(two_number_sum_bfm([3, 5, -4, 8, 11, 1, -1, 6], 10))
