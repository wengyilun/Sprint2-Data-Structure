"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import array as arr

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = arr.array('i')
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)


    def dequeue(self):
        if self.size == 0:
            return
        self.size -= 1
        removed = self.storage[0]
        self.storage.remove(self.storage[0])
        return removed

    def __str__(self):
        output = '['
        count = self.size
        while count > 0:
            output += "," + str(self.storage[count - 1])
            count -= 1
        output += "]"
        return output

q = Queue()
q.enqueue(100)
q.enqueue(101)
q.enqueue(105)
print(q)
q.dequeue()
print(q)
