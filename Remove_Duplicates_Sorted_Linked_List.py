"""
  You're given the head of a Singly Linked List whose nodes are in sorted order
  with respect to their values. Write a function that returns a modified version
  of the Linked List that doesn't contain any nodes with duplicate values. The
  Linked List should be modified in place (i.e., you shouldn't create a brand
  new list), and the modified Linked List should still have its nodes sorted
  with respect to their values.

  Sample Input = 1 -> 1 -> 3 -> 4 -> 4 -> 4 -> 5 -> 6 -> 6
  Sample Output = 1 -> 3 -> 4 -> 5 -> 6
"""


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


# O(n) time | O(1) space - where n is the number of nodes in the Linked List
def remove_duplicates_from_linked_list(linkedList):
    if linkedList is None or linkedList.next is None:
        return linkedList
    current_node = linkedList
    while current_node.next:
        next_node = current_node.next
        if current_node.value == next_node.value:
            current_node.next = next_node.next
        else:
            current_node = current_node.next
    return linkedList
