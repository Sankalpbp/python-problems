def find_max(arr):
    if len(arr) == 0:
        return float('-inf')

    return max(arr[0], find_max(arr[1:]))

print(find_max([1, 2, 3]))
print(find_max([1, 3, 2]))
print(find_max([3, 1, 2]))
