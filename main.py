import pygame
import random

pygame.init()

import sortingUtils
from sortingUtils import colorDataSet
from bubbleSortAlgorithm import bubbleSort, bubbleSortNoVisible
from bogoSortAlgorithm import bogoSort, bogoSortNoVisible
from miracleSortAlgorithm import miracleSort, miracleSortNoVisible
from stalinSortAlgorithm import stalinSort, stalinSortNoVisible
from selectionSortAlgorithm import selectionSort, selectionSortNoVisible
from mergeSortAlgorithm import mergeSort, mergeSortNoVisible
from insertionSortAlgorithm import insertionSort, insertionSortNoVisible

WIDTH, HEIGHT = 1280, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

data = []

delay = 100

def createTestData(length):
    for x in range(length):
        data.append(x + 1)
    
    random.shuffle(data)

createTestData(50)

def showDataToScreen(array):
    scaleFactor = (HEIGHT - 50) / max(array)
    SCREEN.fill("black")
    gap = WIDTH / len(array)
    for x in range(len(array)):
        if x in sortingUtils.comparedIndices:
            color = "red"
        elif x in sortingUtils.selectedIndices:
            color = "green"
        else:
            color = "white"
        #array[x] * scaleFactor
        rect = (x * gap, HEIGHT - (array[x] * scaleFactor), gap, array[x] * scaleFactor)
        pygame.draw.rect(SCREEN, color, rect)

def displayStats():
    font = pygame.font.SysFont('Times New Roman', 20)
    stats_text = font.render(f"Algorithm: {sortingUtils.algorithmName} | Swaps: {sortingUtils.swaps} | Comparisons: {sortingUtils.comparisons} | Visual Delay: {delay}ms | Visual Time: {sortingUtils.sortTimeVisual: .2f}s | Sort Time: {sortingUtils.sortTime * 1000: .5f} ms", True, (255, 255, 255))
    SCREEN.blit(stats_text, (10, 10))

def main():
    running = True

    sortingAlgorithms = {
    "Bubblesort": bubbleSort,
    "Bogosort": bogoSort,
    "Miraclesort": miracleSort,
    "Stalinsort": stalinSort,
    "Selectionsort": selectionSort,
    "Mergesort": mergeSort
    }

    selectedSort = "Stalinsort"
    generator = sortingAlgorithms[selectedSort]
    if selectedSort == "Mergesort":
        generatorFunc = generator(data, delay, 0, len(data) - 1)
    else:
        generatorFunc = generator(data, delay)
    sortingUtils.colorAnim = None

    if selectedSort == "Bubblesort":
        bubbleSortNoVisible(data)
    elif selectedSort == "Bogosort":
        bogoSortNoVisible(data)
    elif selectedSort == "Miraclesort":
        miracleSortNoVisible(data)
    elif selectedSort == "Stalinsort":
        stalinSortNoVisible(data)
    elif selectedSort == "Selectionsort":
        selectionSortNoVisible(data)
    elif selectedSort == "Mergesort":
        mergeSortNoVisible(data, 0, len(data) - 1)

    sortingUtils.algorithmName = selectedSort

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    sortingUtils.sorting = not sortingUtils.sorting
        
        if sortingUtils.sorting:
            try:
                if sortingUtils.colorAnim is None:
                    next(generatorFunc)
                else:
                    next(sortingUtils.colorAnim)
            except StopIteration:
                if sortingUtils.colorAnim is None:
                        sortingUtils.colorAnim = colorDataSet(data, len(data))
                else:
                    sortingUtils.colorAnim = None
                    sortingUtils.sorting = False

        SCREEN.fill("black")

        showDataToScreen(data)
        displayStats()
        pygame.display.flip()

if __name__ == "__main__":
    main()