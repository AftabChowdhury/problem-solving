def two_number_sum_bfm(array, targetSum):
    result = []
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            sum = array[i] + array[j]
            if sum == targetSum:
                result.append(array[i])
                result.append(array[j])
    return result


def two_number_sum_binary_search(array, targetSum):
    array.sort()
    result = []
    for i in range(0, len(array) - 1):
        first_num = array[i]
        second_num = targetSum - first_num
        low = i + 1
        high = len(array) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if second_num == array[mid]:
                result.append(first_num)
                result.append(second_num)
                return result
            elif second_num < array[mid]:
                high = mid - 1
            elif second_num > array[mid]:
                low = mid + 1
    return result


def two_number_sum_hash_map(array, targetSum):
    dict_numbers = {}
    for first_num in array:
        second_num = targetSum - first_num
        if second_num in dict_numbers:
            return [first_num, second_num]
        else:
            dict_numbers[first_num] = True
    return []


print(two_number_sum_bfm([3, 5, -4, 8, 11, 1, -1, 6], 10))
print(two_number_sum_binary_search([3, 5, -4, 8, 11, 1, -1, 6], 10))
print(two_number_sum_hash_map([3, 5, -4, 8, 11, 1, -1, 6], 10))
