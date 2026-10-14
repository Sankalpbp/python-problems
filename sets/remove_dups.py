def remove_duplicates(arr):
    seen = set()

    for element in arr:
        seen.add(element)

    return list(seen)

print(remove_duplicates([1, 1, 2]))
print(remove_duplicates([1, 1, 3, 3]))
