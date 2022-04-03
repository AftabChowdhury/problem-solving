class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        return self

    def contains(self, value):
        if value == self.value:
            return True
        elif value < self.value:
            if self.left is None:
                return False
            self.left.contains(value)
        elif value > self.value:
            if self.right is None:
                return False
            self.right.contains(value)

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        return self
