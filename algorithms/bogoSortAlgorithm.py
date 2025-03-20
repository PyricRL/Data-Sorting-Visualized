import random
import time

import sortingUtils
from sortingUtils import isSorted, wait

def bogoSort(array, delay):
    startTime = time.perf_counter()
    while not isSorted(array) and sortingUtils.sorting:
        wait(delay)
        sortingUtils.swaps += 1
        random.shuffle(array)
        sortingUtils.swapDataSound.play()
        sortingUtils.sortTimeVisual = time.perf_counter() - startTime
        yield

def bogoSortNoVisible(array):
    timeArray = array.copy()
    while not isSorted(timeArray) and sortingUtils.sorting:
        random.shuffle(array)
    
    sortingUtils.sortTime = float('inf')