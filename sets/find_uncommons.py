def get_uncommons(arr1, arr2):

    seen1 = set()
    for element in arr1:
        seen1.add(element)

    result = []

    for element in arr2:
        if element not in seen1:
            result.append(element)

    for element in seen1:
        if element not in arr2:
            result.append(element)

    return result

print(get_uncommons([1, 2, 3], [2, 4]))
print(get_uncommons([1, 2, 3], [2, 3, 1]))
