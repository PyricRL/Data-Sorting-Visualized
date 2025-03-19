from sortingUtils import *

def bubbleSort(array, delay):
    global sorting
    while not isSorted(array) and sorting == True:
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                print(array)
                wait(delay)
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
                    yield
    sorting = False