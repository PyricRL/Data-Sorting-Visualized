import time

import sortingUtils
from sortingUtils import wait

startTime = 0

def countingSort(array, exp1, delay):
    global startTime
    startTime = time.perf_counter()

    n = len(array)

    output = [0] * (n)

    count = [0] * (10)

    sortingUtils.selectedIndices.clear()
    sortingUtils.comparedIndices.clear()

    for i in range(n):
        index = array[i] // exp1
        count[index % 10] += 1
        sortingUtils.selectedIndices.append(i)

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = array[i] // exp1
        output[count[index % 10] - 1] = array[i]
        count[index % 10] -= 1
        i -= 1

        sortingUtils.swaps += 1
        sortingUtils.swapDataSound.play()
        sortingUtils.selectedIndices.append(i)
        wait(delay)

    i = 0
    for i in range(0, len(array)):
        array[i] = output[i]

        sortingUtils.swaps += 1
        sortingUtils.swapDataSound.play()
        sortingUtils.comparedIndices.append(i)
        yield
        wait(delay)
        sortingUtils.sortTimeVisual = time.perf_counter() - startTime

def radixSort(array, delay):
    max1 = max(array)

    exp = 1
    while max1 / exp >= 1:
        yield from countingSort(array, exp, delay)
        exp *= 10

def countingSortNoVisible(array, exp1):
    timeArray = array.copy()
    n = len(timeArray)

    output = [0] * (n)

    count = [0] * (10)

    for i in range(0, n):
        index = timeArray[i] // exp1
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = timeArray[i] // exp1
        output[count[index % 10] - 1] = timeArray[i]
        count[index % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(timeArray)):
        timeArray[i] = output[i]
    
def radixSortNoVisible(array):
    max1 = max(array)

    exp = 1
    while max1 / exp >= 1:
        countingSortNoVisible(array, exp)
        exp *= 10