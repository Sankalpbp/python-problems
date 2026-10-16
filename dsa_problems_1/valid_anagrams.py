def check_valid(string1 : str, string2 : str):
    mappings_for_s1 = {}
    for char in string1:
        mappings_for_s1[char] = mappings_for_s1.get(char, 0) + 1

    mappings_for_s2 = {}
    for char in string2:
        mappings_for_s2[char] = mappings_for_s2.get(char, 0) + 1

    if len(mappings_for_s2) != len(mappings_for_s1):
        return False

    for char, count in mappings_for_s1.items():
        if mappings_for_s2.get(char) is None or count != mappings_for_s2[char]:
            return False

    return True

