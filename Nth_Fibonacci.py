"""
Sample Input: n = 6
Sample Output: 0, 1, 1, 2, 3, 5
"""


# O(n) time | O(n) space
def getNthFib(n):
    if n == 0 or n == 1:
        return 0
    if n == 2 or n == 3:
        return 1
    fibonacci_array = [0, 1, 1]
    for i in range(3, n):
        sum = fibonacci_array[i - 1] + fibonacci_array[i - 2]
        fibonacci_array.append(sum)
    return sum


print(getNthFib(2))
