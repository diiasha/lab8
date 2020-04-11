import pygame 
flag = False 
pygame.init() 
screen = pygame.display.set_mode((720, 480))  

back = pygame.Surface((720, 480)) 
back.fill((162, 250, 248))                
back = back.convert()      

pygame.draw.arc(back, (131, 52, 235), (0, 0, 720*2.2, (480*2.1)), 0, 3.14)

screen.blit(back, (0, 0)) 
pygame.display.flip()  
while not flag:         
    for event in pygame.event.get():  
        if event.type == pygame.QUIT: 
            flag = True               
