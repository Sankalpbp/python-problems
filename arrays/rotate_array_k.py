def rotate_array(arr, k):

	k = k % len(arr)

	# 1 2 3 4 5
	# 3 4 5 1 2 
	
	temp = []

	for i in range(k):
		temp.append(arr[i])

	# 1 2

	for i in range(k, len(arr)):
		arr[i - k] = arr[i]
	
	# 3 4 5

	for i in range(k):
		arr[len(arr) - k + i] = temp[i]

	print(*arr)

rotate_array([1, 2, 3, 4, 5], 2)

rotate_array([1, 2, 3], 2)

rotate_array([1, 2, 3, 4, 5], 25)
