import time

import sortingUtils
from sortingUtils import wait

startTime = 0

def mergeSort(array, delay, left, right):
    global startTime
    if left == 0 and right == len(array) - 1:
        startTime = time.perf_counter()

    if left < right:
        mid = (left + right) // 2

        yield from mergeSort(array, delay, left, mid)
        yield from mergeSort(array, delay, mid + 1, right)
        yield from merge(array, delay, left, mid, right)
    if left == 0 and right == len(array) - 1:
        sortingUtils.sortTimeVisual = time.perf_counter() - startTime

def merge(array, delay, left, mid, right):
    global startTime
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = array[left + i]

    for j in range(n2):
        R[j] = array[mid + 1 + j]

    i = 0 
    j = 0
    k = left 

    while i < n1 and j < n2:
        sortingUtils.comparedIndices.clear()
        sortingUtils.selectedIndices.clear()

        sortingUtils.selectedIndices.append(k)
        sortingUtils.comparedIndices.append(left + i)
        sortingUtils.comparisons += 1
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
            sortingUtils.comparedIndices.append(mid + 1 + j)
            sortingUtils.swaps += 1
            sortingUtils.swapDataSound.play()
        sortingUtils.sortTimeVisual = time.perf_counter() - startTime
        k += 1
        yield
        wait(delay)

    while i < n1:
        sortingUtils.selectedIndices.append(k)
        sortingUtils.comparedIndices.append(left + i)
        array[k] = L[i]
        i += 1
        k += 1
        sortingUtils.swaps += 1
        sortingUtils.swapDataSound.play()
        yield
        wait(delay)

    while j < n2:
        sortingUtils.selectedIndices.append(k)
        sortingUtils.comparedIndices.append(mid + 1 + j)
        array[k] = R[j]
        j += 1
        k += 1
        sortingUtils.swaps += 1
        sortingUtils.swapDataSound.play()
        yield
        wait(delay)

def mergeSortNoVisible(array, left, right):
    global startTime
    timeArray = array.copy()

    if left == 0 and right == len(timeArray) - 1:
        startTime = time.perf_counter()

    if left < right:
        mid = (left + right) // 2

        mergeSortNoVisible(timeArray, left, mid)
        mergeSortNoVisible(timeArray, mid + 1, right)
        mergeNoVisible(timeArray, left, mid, right)

    if left == 0 and right == len(timeArray) - 1:
        sortingUtils.sortTime = time.perf_counter() - startTime

def mergeNoVisible(array, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = [0] * n1
    R = [0] * n2

    for i in range(n1):
        L[i] = array[left + i]

    for j in range(n2):
        R[j] = array[mid + 1 + j]

    i = 0 
    j = 0
    k = left 

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        array[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = R[j]
        j += 1
        k += 1