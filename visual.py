import data
import pygame

def drawBar(screen , numbers , i_algo , j_algo):
    for i in range(len(numbers)):
        if i == i_algo:
            bar_color = data.red
        elif i == j_algo:
            bar_color = data.green
        else:
            bar_color = data.blue
            
        bar = pygame.Rect(
            i * (data.width / len(numbers)) ,
            data.height - (numbers[i] * 5) ,
            data.width / len(numbers) ,
            data.height
        )
        
        pygame.draw.rect(screen , bar_color , bar)