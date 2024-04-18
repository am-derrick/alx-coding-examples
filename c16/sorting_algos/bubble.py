def bubbleSort(arr):
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if (swapped == False):
            break

arr = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]
print(arr)
bubbleSort(arr)
print(arr)
