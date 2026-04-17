import data
import pygame

def drawBar(screen , numbers):
    for i in range(len(numbers)):
        bar = pygame.Rect(
            i * (data.width / len(numbers)) ,
            data.height - (numbers[i] * 5) ,
            data.width / len(numbers) ,
            data.height
        )
        
        pygame.draw.rect(screen , data.blue , bar)
        
def doneDancing(screen , numbers , i):
    if i >= len(numbers):
        return numbers , i , True
    
    bar = pygame.Rect(
        i * (data.width / len(numbers)) ,
        data.height - (numbers[i] * 5) ,
        data.width / len(numbers) ,
        data.height
    )
    
    pygame.draw.rect(screen , data.green , bar)
    return i