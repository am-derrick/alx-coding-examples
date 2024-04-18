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

# Generate a common array
common_array = [i for i in range(1, 1000001)]  # Array from 1 to 1,000,000

# Target value for search
target_value = 999999

# Measure time for linear search
start_time = time.time()
linear_result = linear_search(common_array, len(common_array), target_value)
end_time = time.time()
linear_time = end_time - start_time

# Measure time for binary search (requires a sorted array)
sorted_common_array = sorted(common_array)
start_time = time.time()
binary_result = binary_search(sorted_common_array, len(sorted_common_array), target_value)
end_time = time.time()
binary_time = end_time - start_time

# Display results
print(f"Linear Search: Index {linear_result} (Time: {linear_time} seconds)")
print(f"Binary Search: Index {binary_result} (Time: {binary_time} seconds)")

