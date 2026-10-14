def two_sum(arr, k):
    elements = {}

    for i in range(len(arr)):
        if (k - arr[i]) in elements:
            return [i, elements[k - arr[i]]]
        else:
            elements[arr[i]] = i

    return []

print(two_sum([1, 2, 3], 3))
print(two_sum([1, 2, 4], 5))
print(two_sum([1, 2, 4], 7))
