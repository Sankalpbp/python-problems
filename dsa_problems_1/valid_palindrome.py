def valid_palindrome(string : str) -> bool:
    i = 0
    j = len(str) - 1

    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1

    return True
