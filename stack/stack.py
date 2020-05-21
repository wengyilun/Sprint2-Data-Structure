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
"""
import array as arr

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = arr.array('i')

    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.append(value)

    def pop(self):
        if self.size == 0:
            return
        self.size -=1
        last_item = self.storage[-1]
        self.storage.pop()
        return last_item

    def __str__(self):
        output = '['
        count = self.size
        while count > 0:
            output += "," + str(self.storage[count - 1])
            count -= 1
        output += "]"
        return output

s = Stack()
s.push(100)
s.push(101)
s.push(105)
print(s)

s.pop()
s.pop()
print(s)
#
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = ?
#
#     def __len__(self):
#         pass
#
#     def push(self, value):
#         pass
#
#     def pop(self):
#         pass


# q = Queue()
# q.enqueue(100)
# q.enqueue(101)
# q.enqueue(105)
# print(q)
# q.dequeue()
# print(q)
