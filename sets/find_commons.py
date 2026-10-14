def get_commons(arr1, arr2):

    seen1 = set()
    seen2 = set()

    for element in arr1:
        seen1.add(element)

    for element in arr2:
        seen2.add(element)

    result = []

    for element in seen1:
        if element in seen2:
            result.append(element)

    return result

print(get_commons([1, 2, 3], [2, 4]))
print(get_commons([1, 2, 3], [2, 3, 1]))
