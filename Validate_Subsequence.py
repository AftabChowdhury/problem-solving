"""
  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.
"""


# O(n) time | O(1) space - where n is the length of the array
def is_valid_subsequence_solution1(array, sequence):
    array_index = 0
    sequence_index = 0
    while sequence_index < len(sequence) and array_index < len(array):
        if sequence[sequence_index] == array[array_index]:
            sequence_index += 1
            array_index += 1
        else:
            array_index += 1
    return sequence_index == len(sequence)


# O(n) time | O(1) space - where n is the length of the array
def is_valid_subsequence_solution2(array, sequence):
    # Write your code here.
    sequence_index = 0
    for value in array:
        if sequence_index == len(sequence):
            break
        if value == sequence[sequence_index]:
            sequence_index += 1
    return sequence_index == len(sequence)


print(is_valid_subsequence_solution1([5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10]))
print(is_valid_subsequence_solution2([5, 1, 22, 25, 6, -1, 8, 10], [1, 1, 6, -1, 10]))
