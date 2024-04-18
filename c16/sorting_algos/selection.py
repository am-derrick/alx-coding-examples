def selectionSort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j

        arr[i], arr[min] = arr[min], arr[i]

arr = [19, 48, 99, 71, 13, 52, 96, 73, 86, 7]
print(arr)
selectionSort(arr)
print(arr)
