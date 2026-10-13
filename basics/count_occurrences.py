def count_occurrences (arr, k):
	count = 0

	for element in arr:
		if element == k:
			count += 1

	return count


print(count_occurrences([1, 2, 3], 2))
print(count_occurrences([1, 2, 3], 2))
print(count_occurrences([1, 1, 1], 2))
print(count_occurrences([1, 1, 1], 1))
print(count_occurrences([1], 1))
