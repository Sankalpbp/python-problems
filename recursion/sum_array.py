def sum_array(arr : list) -> int:
    if len(arr) == 0:
        return 0

    return arr[0] + sum_array(arr[1:])

print(sum_array([1, 2, 3]))
print(sum_array([1, 2, 3, 4]))
