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

def decideAlgo(choice):
    j = 0
    
    for i in data.choices:
        if choice == data.choices[i]:
            return data.choice_text[j]
        
        j += 1
        
def getMousePos():
    x , y = pygame.mouse.get_pos()
    
    return x , y
 
# Data
numbers = data.numbers
# ==========================

# Var setup
mouse_x = -10
mouse_y = -10
choice = 0
# ==========================
       
# Pygame setup
pygame.init()
screen = pygame.display.set_mode((data.width , data.height))
pygame.display.set_caption("Sorting Visualizer")
running = True
# ==========================================================

# Time and fps
clock = pygame.time.Clock()
fps = 200
running_time = 0
# ==========================

while running:
    screen.fill(data.black)
    
    if choice != 0:
        if status == False:
            if choice == 1:
                if con:
                    yield_pack = algo.bubble.bubbleSort(numbers)
                    con = False
                    
                numbers , i , j , status = next(yield_pack)
            elif choice == 2:
                if con:
                    yield_pack = algo.selection.selectionSort(numbers)
                    con = False
                    
                numbers , i , j , status = next(yield_pack)
            elif choice == 3:
                if con:
                    yield_pack = algo.insertion.insertionSort(numbers)
                    con = False
                
                numbers , i , j , status = next(yield_pack)
            elif choice == 4:
                if con:
                    yield_pack = algo.quick.quickSort(numbers , 0 , len(numbers) - 1)
                    con = False
                    
                try:
                    numbers , i , j , status = next(yield_pack)
                except:
                    status = True
            elif choice == 5:
                if con:
                    yield_pack = algo.Merge.mergeSort(numbers , 0 , len(numbers) - 1)
                    con = False

                try:
                    numbers , i , j , status = next(yield_pack)
                except:
                    status = True
            elif choice == 6:
                if con:
                    yield_pack = algo.bogo.bogoSort(numbers)
                    con = False
                
                try:
                    numbers , i , j , status = next(yield_pack)
                except:
                    status = True
            elif choice == 7:
                if con:
                    yield_pack = algo.tim.timSort(numbers)
                    con = False
                    
                numbers , i , j , status = next(yield_pack)
                         
            running_time += 0.083
            
        visual.drawBar(screen , numbers , i , j)
        running_time = visual.textRender(screen , text , running_time , status)
    else:
        visual.drawChoices(screen)
        choice = visual.decideChoices(mouse_x , mouse_y)
        
        try:
            i , j = 0 , 0
            text = decideAlgo(choice)
            status = False
            con = True
            
            if choice == 2:
                min_index = i
            # Insertion
            elif choice == 3:
                key = numbers[1]
            # Quick
            elif choice == 4:
                j = len(numbers) - 1
            # Merge
            elif choice == 5:
                j = len(numbers) - 1
        except:
            pass
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x , mouse_y = getMousePos()
    
    pygame.display.flip()
    clock.tick(fps)
    
pygame.quit()
sys.exit()