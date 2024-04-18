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

# E.g.
my_list = [10, 20, 30, 40, 60, 70, 80]
list_size = len(my_list)
val = 30
res_i = binary_search(my_list, list_size, val)

if res_i != -1:
    print(f"{val} found at index {res_i}.")
else:
    print(f"{val} not found.")
