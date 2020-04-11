import pygame

flag = False  
pygame.init() 
screen = pygame.display.set_mode((720, 480))  

back = pygame.Surface((720, 480))
back.fill((162, 250, 248))              
back = back.convert()      

pygame.draw.polygon(back, (131, 52, 235), ((180, 300), (280, 60), (380, 300), (155, 150), (405, 150)), 2)  # by using polygon

screen.blit(back, (0, 0))
pygame.display.flip()  
while not flag: 
    for event in pygame.event.get():    
        if event.type == pygame.QUIT:    
            flag = True                