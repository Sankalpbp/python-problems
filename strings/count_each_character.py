def count_each_character(string : str) -> dict:
    count_for_char = {}

    for char in string:
        count_for_char[char] = count_for_char.get(char, 0) + 1

    return count_for_char

print(count_each_character("abc"))
print(count_each_character("abca"))
print(count_each_character("12ab33n"))
