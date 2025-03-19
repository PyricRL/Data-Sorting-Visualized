from sortingUtils import *

def bubbleSort(array, delay):
    global swaps, comparisons
    while not isSorted(array):
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                wait(delay)
                comparisons += 1
                if array[j] > array[j + 1]:
                    swaps += 1
                    array[j], array[j + 1] = array[j + 1], array[j]
                    yield