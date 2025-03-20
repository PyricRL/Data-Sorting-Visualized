import pygame

pygame.init()

import sortingUtils
from sortingUtils import colorDataSet, createTestData
from sortingManager import SortingManager

WIDTH, HEIGHT = 1280, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

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
        rect = (x * gap, HEIGHT - (array[x] * scaleFactor), 4, 4)
        pygame.draw.rect(SCREEN, color, rect)

def displayStats():
    font = pygame.font.SysFont('Times New Roman', 20)
    stats_text = font.render(f"Algorithm: {sortingUtils.algorithmName} | Swaps: {sortingUtils.swaps} | Comparisons: {sortingUtils.comparisons} | Visual Delay: {sortingUtils.delay}ms | Visual Time: {sortingUtils.sortTimeVisual: .2f}s | Sort Time: {sortingUtils.sortTime * 1000: .5f} ms", True, (255, 255, 255))
    SCREEN.blit(stats_text, (10, 10))


def updateSorting():
    if sortingUtils.sorting:
        try:
            if sortingUtils.colorAnim is None:
                next(sortingManager.generatorFunc)
            else:
                next(sortingUtils.colorAnim)
        except StopIteration:
            if sortingUtils.colorAnim is None:
                sortingUtils.colorAnim = colorDataSet(sortingUtils.data, len(sortingUtils.data))
            else:
                sortingUtils.colorAnim = None
                sortingUtils.sorting = False

def handleEvents():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                sortingUtils.sorting = not sortingUtils.sorting
            if event.key == pygame.K_s:
                sortingManager.switchSort()
    return True

def render():
    SCREEN.fill("black")
    showDataToScreen(sortingUtils.data)
    displayStats()

sortingManager = SortingManager()

def main():
    running = True

    while running:
        running = handleEvents()
        updateSorting()
        render()

        pygame.display.flip()

if __name__ == "__main__":
    main()