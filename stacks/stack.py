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

    def is_empty(self):
        return len(self.arr) == 0

