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

from singly_linked_list import LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __str__(self):
        return f'{self.storage.head.value}'

    def len(self):
        for i in self.storage:
            self.size += 1

    def push(self, value):
        self.storage.add_to_head(value)

    def pop(self):
        pass


linked_list = Stack()

# linked_list.add_to_head(0)
# linked_list.add_to_tail(1)

# print(f'does our LL contain 0? {linked_list.contains(0)}')
# print(f'does our LL contain 1? {linked_list.contains(1)}')

# linked_list.add_to_head(2)
# print(f'the start of the list is {linked_list.head.value}')
linked_list.push(3)
print(linked_list)
