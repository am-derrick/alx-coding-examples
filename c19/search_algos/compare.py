import time

def linear_search(arr, size, value):
    for i in range(size):
        if arr[i] == value:
            return i
    return -1


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

large_list = [i for i in range(1, 1000001)]

target_val = 999999

# For linear search
start_time = time.time()
linear_result = linear_search(large_list, len(large_list), target_val)
end_time = time.time()
linear_time = (end_time - start_time) * 10000

# For binary search
start_time = time.time()
sorted_large_list = sorted(large_list)
binary_result = binary_search(sorted_large_list, len(sorted_large_list), target_val)
end_time = time.time()
binary_time = (end_time - start_time) * 10000

print(f"Linear Search: Index {linear_result} Time it takes is {linear_time}.")
print(f"Binary Search: Index {binary_result} Time it takes is {binary_time}.")
