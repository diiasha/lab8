import pygame 

flag = False 
pygame.init() 
screen = pygame.display.set_mode((720, 480))  
back = pygame.Surface((720, 480)) 
back.fill((0, 0, 0))             
back = back.convert()       


for point in range(0,481,48): 
    pygame.draw.line(back, (point//2, 52, 235), (0,0), (360, point), 1)    
for point in range(0,481,48):
    pygame.draw.line(back, (100, point//2, 170), (720,0), (360, point), 1)    
for point in range(0,481,48): 
    pygame.draw.line(back, (200, 100, point//2), (0,480), (360, point), 1)    
for point in range(0,481,48): 
    pygame.draw.line(back, (60+point//3, 200, 240), (720,480), (360, point), 1)
    
screen.blit(back, (0, 0))  
pygame.display.flip()  
while not flag:         
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:    
            flag = True                

