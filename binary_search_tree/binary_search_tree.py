import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.queue = Queue()
        self.stack = Stack()

    # Insert the given value into the tree
    def insert(self, value):
        
        # check if tree contains values
            # if not 
                # insert value
                # becomes root
        if self.value == None:
            self.value = BinarySearchTree(value)
            return self.value
            
            # if so:
        elif value >= self.value and self.right == None:
            self.right = BinarySearchTree(value)
            return value
        elif value < self.value and self.left == None:
            self.left = BinarySearchTree(value)
            return value

        elif value >= self.value and self.right != None:
            self = self.right
            self.insert(value)
        elif value < self.value and self.left != None:
            self = self.left
            self.insert(value)

                # compare value to current val:
                # if less:
                    # traverse to self.left
                        # doesnt exist:
                            # self.left is val
                        # does exist:
                            # repeat
                # if more:
                    # traverse to self.right
                        # doesnt exist:
                            # self.right is val
                        # does exist:
                            # repeat
                    

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif self.right == None and self.left == None:
            return False
        
        elif target > self.value and self.right != None:
            self = self.right
            return self.contains(target)
        elif target > self.value and self.right == None:
            return False

        elif target < self.value and self.left != None:
            self = self.left
            return self.contains(target)
        elif target < self.value and self.left == None:
            return False
        
        


    # Return the maximum value found in the tree
    def get_max(self):
        if self.right == None:
            return self.value
        else:
            self = self.right
            return self.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # call cb on self.value
        cb(self.value)
        # if left:
        if self.left:
            # call for_each
            self.left.for_each(cb)
        # if right:
        if self.right:
            self.right.for_each(cb)
            # call for_each
        

    # DAY 2 Project -----------------------

    # Depth first plan:
        # use stack
        # push root
        # pop it, store in variable
        # check left/right of variable
        # push both,
        # pop top and store var, check lft and rght
        # rinse and repeat
    # Breadth first plan:
        # add root to queue
        # look right/ left and put in queue
        # get rid of first in
        # repeat

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        self.queue.enqueue(node)
        print(self.queue.storage.head.value.value)
        temp = node
        while self.queue.size > 0:
            if temp.left != None:
                self.queue.enqueue(temp.left)
            if temp.right != None:
                self.queue.enqueue(temp.right)
            self.queue.dequeue()
            if self.queue.storage.head != None:
                temp = self.queue.storage.head.value
                print(temp.value)
            
            
            
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass

# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print(bst)