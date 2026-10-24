def validate(string : str) -> bool:
    stack = []
    mappings = {
        ']': '[',
        '}': '{',
        ')': '('
    }

    for char in string:
        if char in ['(', '[', '{']:
            stack.append(char)
        elif len(stack) == 0:
            return False
        else:
            popped = stack.pop()
            if mappings[char] != popped:
                return False

    return len(stack) == 0

print(validate("()()"))
print(validate("([])()"))
print(validate("(([]){()})"))
print(validate("([)(])"))
