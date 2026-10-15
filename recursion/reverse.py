def reverse(string : str) -> str:
    if len(string) == 0:
        return ""
    return reverse(string[1::]) + string[0]

print(reverse("abc"))
print(reverse("abcd"))
