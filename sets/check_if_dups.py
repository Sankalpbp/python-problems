def check_if_dups(arr):

    seen = set()

    for element in arr:
        if element in seen:
            return True
        seen.add(element)

    return False

print(check_if_dups([1, 2]))
print(check_if_dups([1, 2, 2]))
print(check_if_dups([2, 1, 2]))
