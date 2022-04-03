"""

  The distance between a node in a Binary Tree and the tree's root is called the
  node's depth.

  Write a function that takes in a Binary Tree and returns the sum of its nodes'
  depths.
"""


# O(n) time | O(h) space - where n is the number of nodes in
# the Binary Tree and h is the height of the Binary Tree
def node_depths(root):
    return get_node_depth(root, 0)


def get_node_depth(node, depth):
    if node is None:
        return 0
    depth += get_node_depth(node.left, depth + 1) + get_node_depth(node.right, depth + 1)
    return depth


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
