def remove_duplicates(arr):
    i = 0
    j = 0

    while j < len(arr):
        if arr[i] == arr[j]:
            j += 1
        else:
            i += 1
            arr[i] = arr[j]
    print(*arr[:i + 1], end=", ")
    print()

remove_duplicates([1, 1, 2])
remove_duplicates([1, 2, 2])
remove_duplicates([1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5])

