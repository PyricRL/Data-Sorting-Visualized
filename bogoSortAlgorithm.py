import random
import time

import sortingUtils
from sortingUtils import isSorted, wait

def bogoSort(array, delay):
    startTime = time.perf_counter()
    originalArray = array.copy()
    while not isSorted(array) and sortingUtils.sorting:
        sortingUtils.swaps += 1
        random.shuffle(array)
        sortingUtils.swapDataSound.play()

        sortingUtils.comparedIndices.clear()

        sortingUtils.sortTimeVisual = time.perf_counter() - startTime

        wait(delay)

        for i in range(len(array)):
            if array[i] != originalArray[i]:
                sortingUtils.comparedIndices.append(i)
        yield
        originalArray = array.copy()


def bogoSortNoVisible(array):
    timeArray = array.copy()
    while not isSorted(timeArray) and sortingUtils.sorting:
        random.shuffle(array)
    
    sortingUtils.sortTime = float('inf')