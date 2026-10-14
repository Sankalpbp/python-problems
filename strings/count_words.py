def convert_words(text : str) -> int:
    return len(text.split(" "))

print(convert_words("hi guys"))
print(convert_words("hi guys, how are you?"))
print(convert_words("hi"))
