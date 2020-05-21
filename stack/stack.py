"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
# """
# import array as arr
#
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = arr.array('i')
#
#     def __len__(self):
#         return self.size
#
#     def push(self, value):
#         self.size += 1
#         self.storage.append(value)
#
#     def pop(self):
#         if self.size == 0:
#             return
#         self.size -=1
#         last_item = self.storage[-1]
#         self.storage.pop()
#         return last_item
#
#     def __str__(self):
#         output = '['
#         count = self.size
#         while count > 0:
#             output += "," + str(self.storage[count - 1])
#             count -= 1
#         output += "]"
#         return output


import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def pop(self):
        if self.size == 0:
            return
        self.size -=1
        return self.storage.remove_from_tail()

    def __str__(self):
        return str(self.storage)

s = Stack()
s.push(100)
s.push(101)
s.push(105)
print(s)

removed = s.pop()
print (removed)
print(s)
removed = s.pop()
print (removed)
print(s)
removed = s.pop()
print (removed)
print(s)