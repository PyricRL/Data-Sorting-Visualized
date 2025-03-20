import time

import sortingUtils
from sortingUtils import wait

startTime = 0

def partition(array, low, high, delay):
    global startTime
    if low == 0 and high == len(array) - 1:
        startTime = time.perf_counter()

    pivot = array[high]
    i = low - 1

    sortingUtils.selectedIndices = [high] 

    for j in range(low, high):
        sortingUtils.comparisons += 1
        
        sortingUtils.comparedIndices = [j, high]
        
        if array[j] < pivot:
            i += 1
            sortingUtils.comparedIndices = [i, j]
            array[i], array[j] = array[j], array[i]
            sortingUtils.swapDataSound.play()
            sortingUtils.swaps += 1
            sortingUtils.sortTimeVisual = time.perf_counter() - startTime
            yield
            wait(delay)
        
        sortingUtils.comparedIndices.clear()
        sortingUtils.selectedIndices.clear()

    array[i + 1], array[high] = array[high], array[i + 1]

    if low == 0 and high == len(array) - 1:
        sortingUtils.sortTimeVisual = time.perf_counter() - startTime

    return i + 1

def quickSort(array, low, high, delay):
    global startTime
    
    if low < high:
        part = yield from partition(array, low, high, delay)

        yield from quickSort(array, low, part - 1, delay)
        yield from quickSort(array, part + 1, high, delay)

def partitionNoVisible(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] < pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
            
    array[i + 1], array[high] = array[high], array[i + 1]

    return i + 1

def quickSortNoVisible(array, low, high):
    timeArray = array.copy()
    if low < high:
        part = partitionNoVisible(timeArray, low, high)

        quickSortNoVisible(timeArray, low, part - 1)
        quickSortNoVisible(timeArray, part + 1, high)