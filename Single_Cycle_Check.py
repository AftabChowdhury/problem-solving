# O(n) time | O(1) space - where n is the length of the input array
def hasSingleCycle(array):
    current_index = 0
    number_of_array_element_check = 0
    while number_of_array_element_check < len(array):
        if number_of_array_element_check > 0 and current_index == 0:
            return False
        number_of_array_element_check += 1
        current_index = get_next_index(current_index, array)
    return current_index == 0


def get_next_index(current_index, array):
    jump = array[current_index]
    next_index = (current_index + jump) % len(array)
    if next_index >= 0:
        return next_index
    else:
        return next_index + len(array)


print(hasSingleCycle([2, 3, 1, -4, -4, 2]))
