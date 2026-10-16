def binary_search(arr : list, start : int, end : int, target : int) -> int:
    if start > end:
        return -1

    mid = start + int((end - start) / 2)
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, start, end - 1, target)
    return binary_search(arr, start + 1, end, target)

print(binary_search([1, 2, 3], 0, 2, 1))
print(binary_search([1, 2, 3], 0, 2, 2))
print(binary_search([1, 2, 3], 0, 2, 3))
print(binary_search([1, 2, 3], 0, 2, 4))

