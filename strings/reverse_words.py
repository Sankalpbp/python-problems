def reverse(text : str) -> str:
    words = text.split(" ")
    result = []

    for word in reversed(words):
        result.append(word)
        result.append(" ")

    result.pop()

    return "".join(result)

print(reverse("sankalp is living in hyderabad"))
print(reverse("arora is also"))
print(reverse("renu has just joined them"))
