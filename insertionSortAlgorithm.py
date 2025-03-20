import time

import sortingUtils
from sortingUtils import isSorted, wait

def insertionSort(array, delay):
    startTime = time.perf_counter()
    while not isSorted(array) and sortingUtils.sorting:
        for i in range(1, len(array)):
            k = array[i]
            j = i - 1

            sortingUtils.selectedIndices.clear()
            sortingUtils.comparedIndices.clear()

            sortingUtils.comparedIndices.append(i)

            sortingUtils.comparisons += 1
            while j >= 0 and k < array[j]:
                sortingUtils.selectedIndices.clear()
                sortingUtils.selectedIndices.append(j)
                array[j + 1] = array[j]
                j -= 1
                sortingUtils.swaps += 1
                sortingUtils.swapDataSound.play()
                sortingUtils.sortTimeVisual = time.perf_counter() - startTime

            array[j + 1] = k
            wait(delay)
            yield

def insertionSortNoVisible(array):
    startTime = time.perf_counter()
    while not isSorted(array) and sortingUtils.sorting:
        for i in range(1, len(array)):
            k = array[i]
            j = i - 1

            while j >= 0 and k < array[j]:
                array[j + 1] = array[j]
                j -= 1

            array[j + 1] = k
    
    sortingUtils.sortTime = time.perf_counter() - startTime