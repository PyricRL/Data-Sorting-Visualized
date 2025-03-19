import random

from sortingUtils import *

def bogoSort(array, delay):
    global swaps, comparisons
    while not isSorted(array):
        wait(delay)
        swaps += 1
        random.shuffle(array)
        yield