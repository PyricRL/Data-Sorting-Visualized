def heapify(array, n, i):
    largest = i 
    l = 2 * i + 1 
    r = 2 * i + 2  

    if l < n and array[l] > array[largest]:
        largest = l

    if r < n and array[r] > array[largest]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)
        yield

def heapSort(arr):
    n = len(arr) 

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] 
        yield from heapify(arr, i, 0)