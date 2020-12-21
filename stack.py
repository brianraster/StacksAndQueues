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

    def push(self, x):
        '''add x to the top of the stack'''
        if not isinstance(x, Node):
            x = Node(x)
        print(f'Adding {x.data} to the top of the stack')
        if self.isEmpty():
            self.stack_pointer = x
        else:
            x.next = self.stack_pointer
            self.stack_pointer = x

    def pop(self):
        '''remove and return the node at the top of the stack'''
        if not self.isEmpty():
            print(f'Removing node on top of the stack')
            curr = self.stack_pointer
            self.stack_pointer = self.stack_pointer.next
            curr.next = None
            return curr.data
        else:
            return "Stack is empty"

    def isEmpty(self):
        '''return True if stack is empty, False if not'''
        return self.stack_pointer == None

    def peek(self):
        '''look at the node on top of the stack'''
        if not self.isEmpty():
            return self.stack_pointer.data

    def __str__(self):
        print("Printing Stack state...")
        to_print = ""
        curr = self.stack_pointer
        while curr is not None:
            to_print += str(curr.data) + "->"
            curr = curr.next
        if to_print:
            print("Stack Pointer")
            print(" |")
            print(" V")
            return "[" + to_print[:-2] + "]"
        return "[]"

my_stack = Stack()
print("Checking if stack is empty:", my_stack.isEmpty())
my_stack.push(1)
time.sleep(2)
my_stack.push(2)
print(my_stack)
time.sleep(2)
my_stack.push(3)
time.sleep(2)
my_stack.push(4)
time.sleep(2)
print("Checking item on top of stack:", my_stack.peek())
time.sleep(2)
my_stack.push(5)
print(my_stack)
time.sleep(2)
print(my_stack.pop())
time.sleep(2)
print(my_stack.pop())
print(my_stack)
time.sleep(2)
my_stack.push(4)
print(my_stack)
time.sleep(2)
