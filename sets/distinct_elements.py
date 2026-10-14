def find_distinct(arr):

    seen = set()

    for element in arr:
        seen.add(element)

    return len(seen)

print(find_distinct([1, 2, 3]))
print(find_distinct([1, 2, 2]))
