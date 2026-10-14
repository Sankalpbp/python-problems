def check_sorted (arr):
	for i in range(len(arr) - 1):
		if (arr[i] > arr[i + 1]):
			return False

	return True

print(check_sorted ([1, 2, 3]))
print(check_sorted ([1, 3, 2]))
print(check_sorted ([1]))
