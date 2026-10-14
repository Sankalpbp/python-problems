def two_sum(arr, k):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == k:
                return [i, j]
    return []

print(two_sum([1, 2, 3], 3))
print(two_sum([1, 2, 4], 5))
print(two_sum([1, 2, 4], 7))
