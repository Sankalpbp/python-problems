from json.decoder import NaN


def max_frequency(arr):
    frequency = {}
    for element in arr:
        frequency[element] = frequency.get(element, 0) + 1

    max_count = 0
    result = NaN

    for element, count in frequency.items():
        if count > max_count:
            max_count = count
            result = element

    return result

print(max_frequency([1, 2, 1]))
print(max_frequency([1, 2, 2, 1, 3, 2]))
print(max_frequency([1, 2, 2, 1, 3]))
