import time

import sortingUtils
from sortingUtils import isSorted, wait

def miracleSort(array, delay):
    startTime = time.perf_counter()
    while not isSorted(array) and sortingUtils.sorting:
        wait(delay)
        sortingUtils.sortTimeVisual = time.perf_counter() - startTime
        wait(delay)
        yield

def miracleSortNoVisible(array):
    sortingUtils.sortTime = float('inf')