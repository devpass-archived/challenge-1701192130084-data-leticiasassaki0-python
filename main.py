class Stack:
    def __init__(self):
        // Add your solution here!

    def push(self, item):
        // Add your solution here!

    def pop(self):
        // Add your solution here!

    def peek(self):
        // Add your solution here!

    def is_empty(self):
        // Add your solution here!

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(f'Pop: {stack.pop()}')  # Expected: 3
    print(f'Peek: {stack.peek()}')  # Expected: 2
    print(f'Is Empty: {stack.is_empty()}')  # Expected: False
