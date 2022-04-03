"""

  Write a function that takes in a Binary Tree and returns a list of its branch
  sums ordered from leftmost branch sum to rightmost branch sum.
"""


# O(n) time | O(n) space - where n is the number of nodes in the Binary Tree
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branch_sums(root):
    sum_list = []
    return get_branch_sum(root, 0, sum_list)


def get_branch_sum(node, sum, sum_list):
    if node is None:
        return sum_list
    sum += node.value
    if node.left is None and node.right is None:
        sum_list.append(sum)
    if node.left is not None:
        get_branch_sum(node.left, sum, sum_list)
    if node.right is not None:
        get_branch_sum(node.right, sum, sum_list)
    return sum_list
