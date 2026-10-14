def convert(string : str) -> str:

    chars = list(string)
    for i in range(len(chars)):
        if 'a' <= chars[i] <= 'z':
            chars[i] = chars[i].upper()

    return "".join(chars)

print(convert("Sankalp"))
print(convert("aAbVcTYQa"))
