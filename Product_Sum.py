"""
  Write a function that takes in a "special" array and returns its product sum.


  A "special" array is a non-empty array that contains either integers or other
  "special" arrays. The product sum of a "special" array is the sum of its
  elements, where "special" arrays inside it are summed themselves and then
  multiplied by their level of depth.

  Sample Input : array =  = [5, 2, [7, -1], 3, [6, [-13, 8], 4]]
  Sample Output = 12
  // calculated as: 5 + 2 + 2 * (7 - 1) + 3 + 2 * (6 + 3 * (-13 + 8) + 4)
"""
# O(n) time | O(d) space - where n is the total number of elements in the array,
# including sub-elements, and d is the greatest depth of "special" arrays in the array
def productSum(array, array_depth=1):
    # Write your code here.
    sum = 0
    for value in array:
        if type(value) is list:
            sum += productSum(value, array_depth+1)
        else:
            sum += value
    return sum * array_depth

