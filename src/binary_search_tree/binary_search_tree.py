"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # take the current value of our node (self.value)
        # compare to the new value we want to insert
        # if new value < self.value
        if self.value > value:
            # if self.left is already taken by a node
            if self.left != None:
                # make that (left) node, call insert
                self.left.insert(value)
            else:
                # set the left to the new node with the new value
                self.left = BSTNode(value)

        # elif new value >= self.value
        elif self.value <= value:
            # if self.right is already taken by node
            if self.right != None:
                # make that (right) node call insert
                self.right.insert(value)
            # set the right child to the new node with new value
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if self.value == target:
            return True
        # compare the target to current value
        # if current value < target
        # found = False
        if self.value > target:
            # check the left substree
            # if you cannot go left, return False
            if self.left is None:
                return False
            found = self.left.contains(target)

        # elif current value >= target
        if self.value <= target:
            # check if right subtree contains target
            # if you cannot go right, return False
            if self.right is None:
                return False
            found = self.right.contains(target)

        return found

    def get_max(self):

        # while(current.right):
        #     current = current.right
        # return current.value

        if self.right is None:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node

    def for_each(self, fn):
        if self.value is None:
            pass
        else:
            fn(self.value)
            if self.left is not None:
                self.left.for_each(fn)
            if self.right is not None:
                self.right.for_each(fn)

    def in_order_print(self):
        if self.left:
            self.left.in_order_print()
        print(self.value)
        if self.right:
            self.right.in_order_print()

    def bft_print(self):
        queue = []
        current = None

        if not self.value:
            pass
        queue.append(self.value)

        if self.left:
            queue.append(self.left)
        if self.right:
            queue.append(self.right)

        print(queue.pop(0))

        while len(queue) != 0:
            current = queue[0]

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

            print(queue.pop(0))

    def dft_print(self):
        queue = []
        queue.append(self)

        while len(queue) != 0:
            current = queue.pop()
            print(current)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass


"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

print("bft_print")
bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_print()
print("post order")
bst.post_order_dft()
