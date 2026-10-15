def is_palindrome(string : str) -> bool:
    if len(string) <= 1:
        return True

    return (string[0] == string[len(string) - 1]
                and is_palindrome(string[1:len(string) - 1]))

print(is_palindrome("abc"))
print(is_palindrome("abaa"))
print(is_palindrome("aba"))
print(is_palindrome("acbca"))
