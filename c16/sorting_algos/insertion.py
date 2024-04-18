def insertionSort(arr):
    for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j>=0 and key < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

arr = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]
print(arr)
insertionSort(arr)
print(arr)
