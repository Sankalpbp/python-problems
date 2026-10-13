def rotate_array(arr):

	# 1 2 3 4
	# 2 3 4 1

	temp = arr[0]
	
	for i in range(len(arr) - 1):
		arr[i] = arr[i + 1]

	arr[len(arr) - 1] = temp
	print(*arr)

rotate_array([1, 2, 3, 4])
rotate_array([1, 2, 3])

