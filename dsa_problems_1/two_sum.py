def two_sum(arr, target):
    mappings = {}

    for i in range(len(arr)):
        if (target - arr[i]) in mappings:
            return [i, mappings[target - arr[i]]]
        else:
            mappings[arr[i]] = i

    return []

print(two_sum([1, 2, 3], 3))
print(two_sum([1, 2, 3], 6))
print(two_sum([1, 2, 3, 4], 6))
