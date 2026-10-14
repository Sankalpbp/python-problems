def find_duplicates(arr):
    frequency = {}

    for element in arr:
        frequency[element] = frequency.get(element, 0) + 1

    result = []
    for number, count in frequency.items():
        if count > 1:
            result.append(number)

    return result

print(find_duplicates([1, 2, 2, 3]))
print(find_duplicates([1, 2, 3]))
print(find_duplicates([1, 2, 3, 3]))
