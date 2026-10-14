def remove_spaces(string : str) -> str:
    return string.replace(" ", "")

print(remove_spaces("a bc d"))
print(remove_spaces(" abcd"))
print(remove_spaces(" abcd "))