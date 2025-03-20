import time

import sortingUtils
from sortingUtils import isSorted, wait

def selectionSort(array, delay):
    startTime = time.perf_counter()
    while not isSorted(array) and sortingUtils.sorting:
        for i in range(len(array) - 1):
            minIdx = i

            sortingUtils.selectedIndices.clear()
            sortingUtils.comparedIndices.clear()

            sortingUtils.selectedIndices.append(minIdx)
            for j in range(i + 1, len(array)):
                sortingUtils.comparisons += 1

                if array[j] < array[minIdx]:
                    minIdx = j
                    sortingUtils.selectedIndices.append(minIdx)
                    sortingUtils.comparedIndices.append(i)
                sortingUtils.sortTimeVisual = time.perf_counter() - startTime
            
            array[i], array[minIdx] = array[minIdx], array[i]
            sortingUtils.swapDataSound.play()
            sortingUtils.swaps += 1
            wait(delay)
            yield

def selectionSortNoVisible(array):
    startTime = time.perf_counter()
    timeArray = array.copy()
    while not isSorted(timeArray) and sortingUtils.sorting:
        for i in range(len(timeArray) - 1):
            minIdx = i
            for j in range(i + 1, len(timeArray)):
                if timeArray[j] < timeArray[minIdx]:
                    minIdx = j
            
            timeArray[i], timeArray[minIdx] = timeArray[minIdx], timeArray[i]
    sortingUtils.sortTime = time.perf_counter() - startTime