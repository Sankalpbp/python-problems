def find_second_max (arr):
	maxi = 0
	second_max = 0

	for element in arr:
		if (element > maxi):
			second_max = maxi
			maxi = element
		elif (element > second_max and element != maxi):
			second_max = element

	return second_max


print(find_second_max ([1, 2, 3, 4]))
print(find_second_max ([1, 2, 2, 4]))
print(find_second_max ([1, 2, 4, 4]))
print(find_second_max ([2, 2, 2, 2]))

