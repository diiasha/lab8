import pygame 

flag = True 
pygame.init() 

screen=pygame.display.set_mode((720,480))   

s = screen.get_size()              
background = pygame.Surface(s)     
background.fill((255, 255, 255))             
background = background.convert()            

ball_x = s[0]//2 
ball_y = s[1]//2        

FPS = 60 
clock = pygame.time.Clock() 
speed = 10

while flag:  
    milliseconds = clock.tick(FPS) 
    for event in pygame.event.get():     
        if event.type == pygame.QUIT:    
            flag = False              
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                flag = False     

    keys = pygame.key.get_pressed()       
    
    if keys[pygame.K_RIGHT] and ball_x + 25 < s[0]:    
        ball_x += speed      
    if keys[pygame.K_LEFT] and ball_x > 25:
        ball_x -= speed      
    if keys[pygame.K_UP] and ball_y > 25:
        ball_y -= speed      
    if keys[pygame.K_DOWN] and ball_y + 25 < s[1]:
        ball_y += speed      

    screen.blit(background, (0, 0)) 
    pygame.draw.circle(screen, (242, 19, 60), (ball_x, ball_y), 25)  
    pygame.display.flip()  
