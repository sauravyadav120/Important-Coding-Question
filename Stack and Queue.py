'''1->Find the next Greater element Using Stack'''
def PrintNGE(arr):
    n = len(arr)
    next_greatest = [-1] * n  
    stack = [] 
    for i in range(n - 1, -1, -1):
        while stack and stack[-1] <= arr[i]:
            stack.pop()
        if stack:
            next_greatest[i] = stack[-1]
        stack.append(arr[i])
    return next_greatest

arr = [4, 5, 2, 10, 8]
print(PrintNGE(arr)) 
'''2- Implement stack using array'''
class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.stack[-1]

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())  # Output: 3
print(stack.pop())   # Output: 3
print(stack.size())  # Output: 2
print(stack.is_empty())  # Output: False
print(stack.pop())   # Output: 2
print(stack.is_empty())  # Output: True
'''Implement Queue using array'''
class Queue:
    def __init__(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.queue.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self.queue[0]

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.front())  # Output: 1
print(queue.dequeue())  # Output: 1
print(queue.dequeue())  # Output: 2
print(queue.size())     # Output: 1
print(queue.is_empty()) # Output: False
print(queue.dequeue())  # Output: 3
print(queue.is_empty()) # Output: True