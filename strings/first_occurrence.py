def find_first_occurrence(string : str, ch) -> int:
    for i in range(len(string)):
       if string[i] == ch:
           return i
    return -1

print(find_first_occurrence("abc", 'a'))
print(find_first_occurrence("abc", 'c'))
print(find_first_occurrence("abc", 'e'))
