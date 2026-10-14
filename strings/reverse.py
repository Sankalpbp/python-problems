def reverse(string : str) -> str:
    i = 0
    j = len(string) - 1

    # Strings are immutable in python - just like Java

    chars = list(string)

    while i < j:
        temp = chars[i]
        chars[i] = chars[j]
        chars[j] = temp

        i += 1
        j -= 1

    return "".join(chars)

print(reverse("abc"))
print(reverse("a"))
print(reverse(""))
