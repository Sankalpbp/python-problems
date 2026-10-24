def find_insert_position(arr: list, k: int) -> int:

    if arr[0] > k:
        return 0

    if arr[len(arr) - 1] < k:
        return len(arr)

    for i in range(len(arr)):
        if arr[i] == k:
            return -1
        elif arr[i] > k:
            return i

    return -1

print(find_insert_position([1, 2, 4], 0))
print(find_insert_position([1, 2, 4], 5))
print(find_insert_position([1, 2, 4], 3))
