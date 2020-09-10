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
        if value < self.value:
            # To the LEFT
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            # To the RIGHT
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target is self.value:
            return True
        else:
            if target < self.value:
                # LEFT
                if self.left is None:
                    return False
                else:
                    return self.left.contains(target)
            else:
                #RIGHT
                if self.right is None:
                    return False
                else:
                    return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # 1: Standard Loop Method
        x = self
        while x.right:
            # Haven't found maximum yet, increment and repeat
            x = x.right
        # Found maximum, return value
        return x.value

        # 2: Loop by Recursion Method
        # if self.right is None:
        #     # Found maximum, return value
        #     return self.value
        # else:
        #     # Not maximum yet, call this function again
        #     return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        # Start with LOW first
        if self.left:
            self.left.in_order_print()
        # At this point, we should've recursively checked through all the lefts to get to the lowest value of each subtree
        # until we cannot find anymore lefts for each node in each subtree, letting us know we're currently at the next
        # relative low value in the order. So print here before searching rights for all the high values.

        # Print the AT VALUE
        print(self.value)

        # Continue with HIGH next
        if self.right:
            self.right.in_order_print()
        # At this point, we should've recursively checked through all the rights to get to the highest value of each subtree
        # The printing will already be taken care of by the print method above for each nested if-statement, though


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # bft uses queues
        nodequeue = []
        # stores the current node (self)
        nodequeue.append(self)
        newrow = nodequeue # Temporary holder, so I can use it to extend nodequeue

        # check to make sure the temporary holder has nodes in it, so we can check their lefts and rights
        while len(newrow) > 0:
            # store temporary queue into internal temporary queue, so we can clear out newrow for while-loop test
            currentrow = newrow
            newrow = []

            # Check the lefts and rights of the internally-stored temporary holder, but append any into the recently cleared queue
            for i in currentrow:
                if i.left:
                    newrow.append(i.left)
                if i.right:
                    newrow.append(i.right)

            # Add any nodes in temporary holder to the main queue
            nodequeue.extend(newrow)

        # Out of while-loop, now just print out the queue
        for x in nodequeue:
            print(x.value)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # dft uses stacks
        nodestack = []
        # stores the current node (self)
        nodestack.append(self)

        while len(nodestack) > 0:
            # Since we're using a stack method, store node at end of stack into place-holder and pop it from stack
            currentnode = nodestack.pop()

            # print place-holder
            print(currentnode.value)

            # Check lefts and rights of place-holder and append it to original stack
            if currentnode.right:
                nodestack.append(currentnode.right)
            if currentnode.left:
                nodestack.append(currentnode.left)

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

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
print("post order")
bst.post_order_dft()  
