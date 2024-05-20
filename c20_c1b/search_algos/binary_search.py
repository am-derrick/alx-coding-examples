def binary_search(arr, size, value):
	low = 0
	high = size - 1
	while low <= high:
		mid = (low + high) // 2
		if arr[mid] == value:
			return mid
		elif arr[mid] < value:
			low = mid + 1
		else:
			high = mid - 1
	return -1


# Example
my_list = [10, 20, 30, 40, 50, 60, 70]
list_size = len(my_list)
val = 30
result = binary_search(my_list, list_size, val)

if result != -1:
	print(f"{val} found at index{result}.")
else:
	print(f"{val} not found.")
