text_blit = text + f"{(running_time / 1000):.3f}"
    
    text_blit = font.render(f"{text_blit}ms" , True , data.white)
    screen.blit(text_blit , (10 , 10))