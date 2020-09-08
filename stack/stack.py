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
from linkedlist import LinkedList
from linkedlist import Node

class Stack:
    def __init__(self):
        self.size = 0
        # self.storage = []
        self.storage = LinkedList()

    def __len__(self):
        return self.size

    def push(self, value):
        # self.size = len(self.storage) # Gets size of array BEFORE appending
        # self.size += 1 # Corrects size to account for value being appended
        # return self.storage.append(value)
        self.size += 1
        return self.storage.add_to_tail(value)

    def pop(self):
        # self.size = len(self.storage) # Gets size of array BEFORE pop
        if self.size <= 0:
            return None
        else:
            # There's at least one element in the array. Correct count for the pop performed below
            self.size -= 1
            # return self.storage.pop()
            return self.storage.remove_tail()
