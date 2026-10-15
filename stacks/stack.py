class Stack:
    def __init__(self):
        self.arr = []

    def push(self, value):
        self.arr.append(value)

    def pop(self):
        element = self.arr.pop()
        return element

    def top(self):
        return self.arr[len(self.arr) - 1]

    def print(self):
        print()
        for element in reversed(self.arr):
            print(element, end=", ")

stack = Stack()
stack.print()
stack.push(1)
stack.push(2)

stack.print()

stack.push(3)

stack.print()

print("popped guy: ", stack.pop())
stack.print()

stack.pop()
stack.print()
print("top guy: ", stack.top())
stack.print()

