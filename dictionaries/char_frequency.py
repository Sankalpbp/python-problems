def char_frequency(string : str) -> dict:
    frequency = {}
    for char in string:
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

print(char_frequency("abcd"))
print(char_frequency("aab"))
