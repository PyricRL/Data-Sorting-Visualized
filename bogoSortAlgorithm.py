import random

from sortingUtils import isSorted

def bogoSort(array):
    while not isSorted(array):
        random.shuffle(array)
    return array