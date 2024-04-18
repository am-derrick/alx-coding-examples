def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def quickSort(arr, low, high):
    if low < high:
        new = partition(arr, low, high)
        quickSort(arr, low, new - 1)
        quickSort(arr, new + 1, high)


arr = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]
print(arr)
n = len(arr)
quickSort(arr, 0, n - 1)
print(arr)
