def equals(string1 : str, string2 : str) -> bool:

    if string1.__ne__(string2):
        return False

    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False

    return True

print(equals("abc", "abc"))
print(equals("def", "abc"))
print(equals("abb", "abc"))
