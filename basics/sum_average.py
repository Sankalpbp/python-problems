def sum_average(arr):
	sum = 0

	for element in arr:
		sum += element

	return [ sum, (sum/len(arr)) ]

print (sum_average([1, 2, 3]))
