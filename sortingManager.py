import random
import sortingUtils
from sortingUtils import createTestData
from bubbleSortAlgorithm import bubbleSort, bubbleSortNoVisible
from bogoSortAlgorithm import bogoSort, bogoSortNoVisible
from miracleSortAlgorithm import miracleSort, miracleSortNoVisible
from stalinSortAlgorithm import stalinSort, stalinSortNoVisible
from selectionSortAlgorithm import selectionSort, selectionSortNoVisible
from mergeSortAlgorithm import mergeSort, mergeSortNoVisible
from insertionSortAlgorithm import insertionSort, insertionSortNoVisible

class SortingManager:
    def __init__(self):
        self.sortingAlgorithms = {
            "Bubble Sort": (bubbleSort, bubbleSortNoVisible),
            "Bogo Sort": (bogoSort, bogoSortNoVisible),
            "Miracle Sort": (miracleSort, miracleSortNoVisible),
            "Stalin Sort": (stalinSort, stalinSortNoVisible),
            "Selection Sort": (selectionSort, selectionSortNoVisible),
            "Merge Sort": (mergeSort, mergeSortNoVisible),
            "Insertion Sort": (insertionSort, insertionSortNoVisible),
        }

        self.sortNames = list(self.sortingAlgorithms.keys())
        self.currentSortIndex = 0
        self.algorithmName = self.sortNames[self.currentSortIndex]
        self.generatorFunc = None
        self.resetSort()
    
    def resetSort(self):
        self.algorithmName = self.sortNames[self.currentSortIndex]
        sortingUtils.algorithmName = self.algorithmName
        sortingUtils.data.clear()
        createTestData(1024)
        sortingUtils.sorting = False
        sortingUtils.comparedIndices.clear()
        sortingUtils.selectedIndices.clear()
        sortingUtils.swaps = 0
        sortingUtils.comparisons = 0
        sortingUtils.colorAnim = None

        sortFunc, noVisualSortFunc = self.sortingAlgorithms[self.algorithmName]

        if self.algorithmName == "Merge Sort":
            self.generatorFunc = sortFunc(sortingUtils.data, sortingUtils.delay, 0, len(sortingUtils.data) - 1)
            noVisualSortFunc(sortingUtils.data, 0, len(sortingUtils.data) - 1)
        else:
            self.generatorFunc = sortFunc(sortingUtils.data, sortingUtils.delay)
            noVisualSortFunc(sortingUtils.data)

    def switchSort(self):
        self.currentSortIndex = (self.currentSortIndex + 1) % len(self.sortNames)
        self.resetSort()
        sortingUtils.sorting = False
        sortingUtils.sortTimeVisual = 0