import time

import sortingUtils
from sortingUtils import wait

startTime = 0

def heapify(array, n, i, delay):
    largest = i 
    l = 2 * i + 1 
    r = 2 * i + 2 

    sortingUtils.selectedIndices.clear()
    sortingUtils.comparedIndices.clear()

    sortingUtils.selectedIndices.append(largest) 

    if l < n and array[l] > array[largest]:
        largest = l
        sortingUtils.selectedIndices.append(largest)

    if r < n and array[r] > array[largest]:
        largest = r
        sortingUtils.selectedIndices.append(largest)
    
    sortingUtils.comparisons += 1

    if largest != i:
        sortingUtils.comparedIndices.append(i)
        sortingUtils.swaps += 1
        array[i], array[largest] = array[largest], array[i]
        yield from heapify(array, n, largest, delay)
        sortingUtils.sortTimeVisual = time.perf_counter() - startTime
        yield
        wait(delay)

def heapSort(array, delay):
    global startTime
    startTime = time.perf_counter()
    n = len(array) 

    for i in range(n // 2 - 1, -1, -1):
        yield from heapify(array, n, i, delay)

    for i in range(n - 1, 0, -1):
        array[0], array[i] = array[i], array[0]
        sortingUtils.swaps += 1
        yield from heapify(array, i, 0, delay)

def heapifyNoVisible(array, n, i):
    largest = i 
    l = 2 * i + 1 
    r = 2 * i + 2 

    if l < n and array[l] > array[largest]:
        largest = l

    if r < n and array[r] > array[largest]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapifyNoVisible(array, n, largest)

def heapSortNoVisible(array):
    startTime = time.perf_counter()
    timeArray = array.copy()
    n = len(timeArray)

    for i in range(n // 2 - 1, -1, -1):
        heapifyNoVisible(timeArray, n, i)

    for i in range(n - 1, 0, -1):
        timeArray[0], timeArray[i] = timeArray[i], timeArray[0]
        heapifyNoVisible(timeArray, i, 0)

    sortingUtils.sortTime = time.perf_counter() - startTime