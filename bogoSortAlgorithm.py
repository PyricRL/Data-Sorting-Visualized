import random

from sortingUtils import *

def bogoSort(array):
    while not isSorted(array):
        random.shuffle(array)
    return array