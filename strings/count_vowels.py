def count_vowels(string : str) -> int:
    count = 0
    vowels = ['a', 'e', 'i', 'o', 'u']
    for element in string:
        if element in vowels:
            count += 1

    return count

print(count_vowels("abc"))
print(count_vowels("dbc"))
