def linear_search(arr, size, value):
    for i in range(size):
        if arr[i] == value:
            return i
    return -1


# Example:
new_list = [10, 20, 50, 70, 80]
list_size = len(new_list)
val = 70
res = linear_search(new_list, list_size, val)

if res != -1:
    print(f"Value {val} found at index {res}.")
else:
    print(f"Value {val} not found.")
