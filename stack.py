import time

class Node:
    def __init__(self, data=None):
        '''initialize node with data and next pointer'''
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        '''initialize stack with stack pointer'''
        print('Stack created')
        self.stack_pointer = None
