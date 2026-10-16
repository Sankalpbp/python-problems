def find_first_unique(string : str) -> int:
    mappings = {}

    for char in string:
        mappings[char] = mappings.get(char, 0) + 1

    for i in range(len(string)):
        if mappings[string[i]] == 1:
            return i

    return -1
