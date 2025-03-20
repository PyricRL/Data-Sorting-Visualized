import time

import sortingUtils
from sortingUtils import isSorted, wait

def bubbleSort(array, delay):
    startTime = time.perf_counter()
    while not isSorted(array) and sortingUtils.sorting:
        swapped = False
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                sortingUtils.comparisons += 1

                sortingUtils.selectedIndices.clear()
                sortingUtils.comparedIndices.clear()

                sortingUtils.selectedIndices.append(j + 1)
                if array[j] > array[j + 1]:
                    sortingUtils.swaps += 1
                    sortingUtils.comparedIndices.append(j)
                    array[j], array[j + 1] = array[j + 1], array[j]
                    sortingUtils.swapDataSound.play()
                    swapped = True
                    yield
                sortingUtils.sortTimeVisual = time.perf_counter() - startTime
                wait(delay)
        if not swapped:
            break

def bubbleSortNoVisible(array):
    timeArray = array.copy()
    startTime = time.perf_counter()
    while not isSorted(timeArray):
        swapped = False
        for i in range(len(timeArray)):
                for j in range(0, len(timeArray) - i - 1):
                    if timeArray[j] > timeArray[j + 1]:
                        timeArray[j], timeArray[j + 1] = timeArray[j + 1], timeArray[j]
                        swapped = True
        if not swapped:
            break
    sortingUtils.sortTime = time.perf_counter() - startTime