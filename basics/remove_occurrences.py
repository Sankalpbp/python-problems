def remove_occurrences (arr, k):
	for element in arr:
		if element == k:
			arr.remove(element)

	return arr

print(remove_occurrences([1, 2, 3, 1], 1))
