"""

  Write a function that takes in a Binary Search Tree (BST) and a target integer
  value and returns the closest value to that target value contained in the BST.

  You can assume that there will only be one closest value.
"""


# Average: O(log(n)) time | O(1) space
# Worst: O(n) time | O(1) space
def find_closest_value_In_bst(tree, target):
    return get_closest_value(tree, target, tree.value)


def get_closest_value(tree, target, closest_value):
    current_tree = tree
    while current_tree is not None:
        if abs(target - current_tree.value) < abs(target - closest_value):
            closest_value = current_tree.value
        if target < current_tree.value:
            current_tree = current_tree.left
        elif target > current_tree.value:
            current_tree = current_tree.right
        else:
            break
    return closest_value


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
