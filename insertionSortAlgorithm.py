import time

import sortingUtils
from sortingUtils import isSorted, wait

def insertionSort(array, delay):
    i = 1
    while not isSorted(array):
        while i < len(array):
            k = i
            while k > 0 and array[k - 1] > array[k]:
                array[k - 1], array[k] = array[k], array[k - 1]
    
    i += 1

data = [5, 3, 2, 1, 4]

insertionSort(data, 1)

print(data)