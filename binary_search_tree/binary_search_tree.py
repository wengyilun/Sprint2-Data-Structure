import sys
sys.path.append('../queue')
from queue import Queue


# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = DoublyLinkedList()
#
#     def __len__(self):
#         return self.size
#
#     def enqueue(self, value):
#         self.size += 1
#         self.storage.add_to_tail(value)
#
#     def dequeue(self):
#         if self.size == 0:
#             return
#         self.size -= 1
#         return self.storage.remove_from_head()
#
#     def __str__(self):
#         return str(self.storage)

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

# sys.path.append('../stack')
# from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        new_node = BSTNode(value)
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = new_node
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = new_node


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if self.left is None:
                return False

            return self.left.contains(target)

        else:
            if self.right is None:
                return False

            return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        current = self
        max_value = current.value

        if current.right is None:
            return self.value

        while current:
            if max_value < current.value:
                max_value = current.value
            current = current.right

        return max_value



    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        queue = [self]
        while len(queue) > 0:
            popped = queue.pop()

            if popped is None:
                continue
            fn(popped.value)
            queue.append(popped.left)
            queue.append(popped.right)


    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is not None:
            self.in_order_print(node.left)
            print(node.value)
            self.in_order_print(node.right)


    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = [node]
        while len(queue) > 0:
            popped = queue.pop(0)
            if popped is None:
                continue
            print(popped.value)
            queue.append(popped.left)
            queue.append(popped.right)
    # def bft_print(self, node):
    #     q = Queue()
    #     q.enqueue(node)
    #     while len(q) > 0:
    #         popped = q.dequeue()
    #         if popped is None:
    #             continue
    #         print(popped.value)
    #         q.enqueue(popped.left)
    #         q.enqueue(popped.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        queue = [node]
        while len(queue) > 0:
            popped = queue.pop(0)
            if popped is None:
                continue
            print(popped.value)
            queue.insert(0, popped.right)
            queue.insert(0, popped.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is not None:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is not None:
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)


bst = BSTNode(1)
bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)
# print(bst)
# bst.in_order_print(bst)
bst.pre_order_dft(bst)

