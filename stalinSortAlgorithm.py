import time

import sortingUtils
from sortingUtils import isSorted, wait

def stalinSort(array, delay):
    i = 0
    startTime = time.perf_counter()
    while not isSorted(array):
        while i < len(array) - 1:
            sortingUtils.comparisons += 1
            sortingUtils.comparedIndices.clear()
            sortingUtils.selectedIndices.clear()
            if array[i] > array[i + 1]:
                sortingUtils.comparedIndices.append(i + 1)
                sortingUtils.selectedIndices.append(i)
                array.pop(i + 1)
                sortingUtils.swapDataSound.play()
                sortingUtils.sortTimeVisual = time.perf_counter() - startTime
                yield
            else:
                i += 1
            wait(delay)

def stalinSortNoVisible(array):
    i = 0
    timeArray = array.copy()
    startTime = time.perf_counter()
    while i < len(timeArray) - 1:
        if timeArray[i] > timeArray[i + 1]:
            timeArray.pop(i + 1)
            sortingUtils.sortTime = time.perf_counter() - startTime
        else:
            i += 1