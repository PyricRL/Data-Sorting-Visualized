import random

import sortingUtils
from sortingUtils import isSorted, wait

def bogoSort(array, delay):
    while not isSorted(array) and sortingUtils.sorting:
        wait(delay)
        sortingUtils.swaps += 1
        random.shuffle(array)
        yield