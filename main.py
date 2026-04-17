import pygame
import algo
import visual
import data
import sys
import time

def choiceAlgo(choice):
    for i in data.choices:
        if choice == data.choices[i]:
            return data.algo[i][0] , data.algo[i][1]
        
def choosing():
    print("Choose:\n")
    print("1. Bubble sort")
    print("2. Selection sort")
    print("3. Insertion sort")
    print("4. Quick sort")
    print("5. Merge sort")
    
    user = int(input("Choice ?: "))
    
    return user
 
# Data
numbers = data.numbers
# ==========================

# Choices
choice = choosing()
i , j = choiceAlgo(choice)
status = False
text = "Bubble sort: "

# Bubble
# Selection
if choice == 2:
    min_index = i
    text = "Selection sort: "
# Insertion
elif choice == 3:
    key = numbers[1]
    text = "Insertion sort: "
# Quick
elif choice == 4:
    j = len(numbers) - 1
    con = True
    text = "Quick sort: "
# Merge
elif choice == 5:
    j = len(numbers) - 1
    con = True
    text = "Merge sort: "
# ==========================
       
# Pygame setup
pygame.init()
screen = pygame.display.set_mode((data.width , data.height))
pygame.display.set_caption("Sorting Visualizer")
running = True
font = pygame.font.SysFont(None , 36)
# ==========================================================

# Time and fps
clock = pygame.time.Clock()
fps = 200
running_time = 0
# ==========================

while running:
    if status == False:
        if choice == 1:
            numbers , i , j , status = algo.bubble.bubbleSort(numbers , i , j)
        elif choice == 2:
            numbers , i , j , status , min_index = algo.selection.selectionSort(numbers ,
                                                                                i , j , 
                                                                                min_index)
        elif choice == 3:
            numbers , i , j , status , key = algo.insertion.insertionSort(numbers , 
                                                                          i , j , 
                                                                          key)
        elif choice == 4:
            if con:
                yield_pack = algo.quick.quickSort(numbers ,
                                                i , j)
                con = False
            else:
                try:
                    numbers , i , j , status = next(yield_pack)
                except:
                    status = True
        elif choice == 5:
            if con:
                yield_pack = algo.Merge.mergeSort(numbers , 
                                                  i , j)
                con = False
            else:
                try:
                    numbers , i , j , status = next(yield_pack)
                except:
                    status = True
                    
        running_time += 0.083
    
    screen.fill(data.black)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    visual.drawBar(screen , numbers , i , j)
        
    text_blit = text + f"{(running_time / 1000):.3f}"
    
    text_blit = font.render(f"{text_blit}ms" , True , data.white)
    screen.blit(text_blit , (10 , 10))
    
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
sys.exit()