def find_first_unique(arr):

    frequency = {}

    for element in arr:
        frequency[element] = frequency.get(element, 0) + 1

    for element in arr:
        if frequency[element] == 1:
            return element

    return -1

print(find_first_unique([1, 2, 3]))
print(find_first_unique([2, 2, 1, 3, 3]))
print(find_first_unique([2, 1, 3, 3]))
