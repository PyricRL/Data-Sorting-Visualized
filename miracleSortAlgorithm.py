import sortingUtils
from sortingUtils import isSorted, wait

def miracleSort(array, delay):
    while not isSorted(array):
        wait(delay)
        sortingUtils.swapDataSound.play()
        yield
