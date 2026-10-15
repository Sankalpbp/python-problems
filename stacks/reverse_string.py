from stack import Stack

def reverse(string : str) -> str:

    stack = Stack()

    for char in string:
        stack.push(char)

    chars = []
    while not stack.is_empty():
        chars.append(stack.pop())

    return "".join(chars)

print(reverse("abc"))
print(reverse("ac"))
print(reverse("aca"))
