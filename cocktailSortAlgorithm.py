import time

import sortingUtils
from sortingUtils import isSorted, wait

def cocktailSort(array, delay):
    swapped = True
    start = 0
    end = len(array) - 1
    startTime = time.perf_counter()

    while not isSorted(array) and sortingUtils.sorting:
        swapped = False

        for i in range(start, end):
            sortingUtils.comparisons += 1
            sortingUtils.selectedIndices.clear()
            sortingUtils.comparedIndices.clear()
            sortingUtils.selectedIndices.append(i)
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                sortingUtils.swaps += 1
                sortingUtils.comparedIndices.append(i + 1)
                sortingUtils.swapDataSound.play()
                swapped = True
                yield
            sortingUtils.sortTimeVisual = time.perf_counter() - startTime
            wait(delay)

        if not swapped:
            break
    
        swapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            sortingUtils.comparisons += 1
            sortingUtils.selectedIndices.clear()
            sortingUtils.comparedIndices.clear()
            sortingUtils.selectedIndices.append(i)
            if (array[i] > array[i + 1]):
                array[i], array[i + 1] = array[i + 1], array[i]
                sortingUtils.swaps += 1
                sortingUtils.comparedIndices.append(i + 1)
                sortingUtils.swapDataSound.play()
                swapped = True
                yield
            sortingUtils.sortTimeVisual = time.perf_counter() - startTime
            wait(delay)

        start = start + 1

def cocktailSortNoVisible(array):
    timeArray = array.copy()
    startTime = time.perf_counter()
    swapped = False
    start = 0
    end = len(array) - 1

    while not isSorted(array) and sortingUtils.sorting:
        swapped = False

        for i in range(start, end):
            if (timeArray[i] > timeArray[i + 1]):
                timeArray[i], timeArray[i + 1] = timeArray[i + 1], timeArray[i]
                swapped = True

        if not swapped:
            break
    
        swapped = False

        end = end - 1

        for i in range(end - 1, start - 1, -1):
            if (timeArray[i] > timeArray[i + 1]):
                timeArray[i], timeArray[i + 1] = timeArray[i + 1], timeArray[i]
                swapped = True

        start = start + 1
    sortingUtils.sortTime = time.perf_counter() - startTime