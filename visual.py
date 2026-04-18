import data
import pygame

def timeTime(running_time , status):
    if status == False:
        running_time += 0.083
        
    return running_time

def textRender(screen , text , running_time , status):
    font = pygame.font.SysFont(None , 36)
    running_time = timeTime(running_time , status)
    text_blit = text + f"{(running_time / 1000):.3f}"
    text_blit = font.render(f"{text_blit}ms" , True , data.white)
    screen.blit(text_blit , (10 , 10))
    return running_time

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
        
def drawChoices(screen):
    j = 0
    
    for i in data.choices:
        if (data.choices[i] - 1) % 4 == 0 and data.choices[i] - 1 != 0:
            j += 1
        
        rect = pygame.Rect(
            ((data.choices[i] - 1) * (data.width // 4)) % data.width ,
            j * (data.height // 4) ,
            200 ,
            100
        )
        
        pygame.draw.rect(screen , data.white , rect , 2)
        font = pygame.font.SysFont(None , 36)
        text = font.render(f"{i}" , True , data.white)
        text_rect = text.get_rect(center = rect.center)
        screen.blit(text , text_rect)
        
def decideChoices(x , y):
    j = 0
    
    for i in data.choices:
        if (data.choices[i] - 1) % 4 == 0 and data.choices[i] - 1 != 0:
            j += 1
        
        rect = pygame.Rect(
            ((data.choices[i] - 1) * (data.width // 4)) % data.width ,
            j * (data.height // 4) ,
            200 ,
            100
        )
        
        if rect.collidepoint((x , y)):
            return data.choices[i]
        
    return 0