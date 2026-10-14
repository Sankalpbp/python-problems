def find_missing(arr):
    n = len(arr)

    missing = []

    for i in range(1, len(arr) + 1):
        if i not in arr:
            missing.append(i)

    return missing

print(find_missing([1, 2, 3]))
print(find_missing([1, 2, 4]))
print(find_missing([2, 2, 3]))
