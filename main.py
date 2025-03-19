import pygame
import random

from bubbleSortAlgorithm import bubbleSort
from bogoSortAlgorithm import bogoSort

WIDTH, HEIGHT = 1280, 700
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

sorting = True

data = []

def createTestData(length):
    for x in range(length):
        data.append(x + 1)
    
    random.shuffle(data)

createTestData(10)

def showDataToScreen(array):
    SCREEN.fill("black")
    gap = WIDTH // len(array)
    for x in range(len(array)):
        rect = (x * gap, HEIGHT - array[x], gap - 1, array[x])
        pygame.draw.rect(SCREEN, "white", rect)

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        showDataToScreen(data)

        pygame.display.flip()

    bogoSort(data)

if __name__ == "__main__":
    main()