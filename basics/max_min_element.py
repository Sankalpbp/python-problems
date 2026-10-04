
def minimum_maximum (arr):
	minimum = arr[0]
	maximum = arr[0]

	for element in arr:
		minimum = min(element, minimum)
		maximum = max(element, maximum)

	return [minimum, maximum]

print ("minimum and maximum elements are: ", minimum_maximum ([1, 2, 3, 4]))
