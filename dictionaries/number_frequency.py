def number_frequency(arr):
    frequency = {}

    for element in arr:
        frequency[element] = frequency.get(element, 0) + 1

    return frequency

print(number_frequency([1, 2, 3]))
print(number_frequency([1, 2, 1, 2, 4, 3]))
