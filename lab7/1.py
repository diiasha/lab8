import pygame 

flag = False 
pygame.init() 
screen=pygame.display.set_mode((720,480)) 
back = pygame.Surface((720, 480))   
back.fill((162, 250, 248))         
back = back.convert()           

pygame.draw.circle(back, (237, 71, 174), (360, 240), 160)

screen.blit(back, (0, 0)) 
pygame.display.flip()  
while not flag:  
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:    
            flag = True                
