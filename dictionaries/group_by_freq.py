def group_by_frequency(arr):
    result = {}
    frequency = {}

    for element in arr:
        frequency[element] = frequency.get(element, 0) + 1

    for element, count in frequency.items():
        if count not in result:
            result[count] = []
        result[count].append(element)

    return result

print(group_by_frequency([1, 1, 2, 3, 3]))
print(group_by_frequency([1, 2, 3]))
print(group_by_frequency([1, 1, 2, 2, 2, 3, 3, 3, 3]))
