def reverse (arr):
	i = 0
	j = len(arr) - 1

	k = 0

	while (i < j):
		temp = arr[i]
		arr[i] = arr[j]
		arr[j] = temp
		i += 1
		j -= 1
	
	print (*arr)

reverse([1, 2, 3])
reverse([1])

