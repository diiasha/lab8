import pygame 

flag = False 
pygame.init() 
screen=pygame.display.set_mode((720,480)) 
back = pygame.Surface((720, 480))   
back.fill((162, 250, 248))         
back = back.convert()

pygame.draw.circle(back, (0,0,0), (360, 240), 100, 10)

pygame.draw.line(back, (0,0,0), (460, 240), (260, 240), 10)

pygame.draw.line(back, (0,0,0), (360, 140), (360, 340), 10)

screen.blit(back, (0, 0)) 
pygame.display.flip()  
while not flag:  
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:    
            flag = True  