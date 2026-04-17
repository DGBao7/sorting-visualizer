import pygame
import algo
import json
import visual
import data
import sys

def choiceAlgo(choice):
    for i in data.choices:
        if choice == data.choices[i]:
            return data.algo[i][0] , data.algo[i][1]

pygame.init()
screen = pygame.display.set_mode((data.width , data.height))
pygame.display.set_caption("Sorting Visualizer")
running = True

clock = pygame.time.Clock()
fps = 60

numbers = data.numbers

choice = 1
i , j = choiceAlgo(choice)
status = False

while running:
    numbers , i , j , status = algo.bubble.bubbleSort(numbers , i , j)
    
    screen.fill(data.black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    visual.drawBar(screen , numbers)
        
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()