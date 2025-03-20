import random

import sortingUtils
from sortingUtils import isSorted, wait

def bogoSort(array):
    while not isSorted(array) and sortingUtils.sorting:
        wait(100)
        sortingUtils.swaps += 1
        random.shuffle(array)
        yield