import pygame
from enum import Enum

# pylint: disable=no-member

pygame.init()
pygame.mixer.init()

##########################################    Upload files    ##########################################

screen_size = (800, 600)
screen = pygame.display.set_mode(screen_size)
icon = pygame.image.load('resources/war.png')
pygame.display.set_icon(icon)
pygame.display.set_caption('Tanks 2D')

green_tank1 = pygame.image.load('resources/green1.png')
green_tank2 = pygame.image.load('resources/green2.png')
blue_tank1 = pygame.image.load('resources/blue1.png')
blue_tank2 = pygame.image.load('resources/blue2.png')
purple_tank1 = pygame.image.load('resources/purple1.png')
purple_tank2 = pygame.image.load('resources/purple2.png')

heart = pygame.image.load('resources/heart.png')

sound_col = pygame.mixer.Sound('resources/collision.wav')
sound_col.set_volume(0.2)
# print(pygame.font.get_fonts())
font = pygame.font.Font('freesansbold.ttf', 25)
sound_shoot = pygame.mixer.Sound('resources/shoot.wav')
sound_shoot.set_volume(0.2)


class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4


##########################################    Bullet    ##########################################


class Bullet:

    def __init__(self, tank):
        sound_shoot.play()
        self.tank = tank
        self.color = tank.color
        self.width = 4
        self.height = 8
        self.direction = tank.direction
        self.speed = 500
        self.lifetime = 0
        self.destroytime = 3  # seconds
        if tank.direction == Direction.RIGHT:
            self.x = tank.x + 3 * tank.width // 2
            self.y = tank.y + tank.width // 2
            self.height, self.width = self.width, self.height

        if tank.direction == Direction.LEFT:
            self.x = tank.x - tank.width // 2
            self.y = tank.y + tank.width // 2
            self.height, self.width = self.width, self.height

        if tank.direction == Direction.UP:
            self.x = tank.x + tank.width // 2
            self.y = tank.y - tank.width // 2

        if tank.direction == Direction.DOWN:
            self.x = tank.x + tank.width // 2
            self.y = tank.y + 3 * tank.width // 2

    def draw(self):
        pygame.draw.ellipse(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, sec):
        self.lifetime += sec

        if self.direction == Direction.RIGHT:
            self.x += round(self.speed * sec)

        if self.direction == Direction.LEFT:
            self.x -= round(self.speed * sec)

        if self.direction == Direction.UP:
            self.y -= round(self.speed * sec)

        if self.direction == Direction.DOWN:
            self.y += round(self.speed * sec)
        self.draw()


##########################################    Tanks    ##########################################

#! hukjh
#? kjn
#* jknkjn
#todo kj
#//jkjnjknjknjk


class Tank:

    def __init__(self, x, y, speed, max_lifes, color, name, image1, image2, d_right=pygame.K_RIGHT, d_left=pygame.K_LEFT, d_up=pygame.K_UP,
                 d_down=pygame.K_DOWN, fire=pygame.K_SPACE):
        self.x = x
        self.y = y
        self.speed = speed
        self.color = color
        self.width = 32
        self.lifes = max_lifes
        self.direction = Direction.RIGHT
        self.fire_key = fire
        self.image1 = image1
        self.image2 = image2
        self.animation = True
        self.name = name

        self.KEY = {d_right: Direction.RIGHT, d_left: Direction.LEFT, d_up: Direction.UP, d_down: Direction.DOWN}
    
    def draw(self):
        if self.animation:
            sprite = self.image1
            self.animation = False
        else:
            sprite = self.image2
            self.animation = True

        if self.direction == Direction.RIGHT:
            sprite = pygame.transform.rotate(sprite, -90)
        if self.direction == Direction.LEFT:
            sprite = pygame.transform.rotate(sprite, 90)
        if self.direction == Direction.DOWN:
            sprite = pygame.transform.rotate(sprite, 180)

        screen.blit(sprite, (round(self.x), round(self.y)))
       

    def changeDirection(self, direction):
        self.direction = direction

    def move(self, sec):
        global tanks

        dx = dy = 0

        if self.x < -self.width:
            self.x = screen_size[0]
        if self.x > screen_size[0]:
            self.x = -self.width
        
        if self.y < -self.width:
            self.y = screen_size[1]
        if self.y > screen_size[1]:
            self.y = -self.width

        speed = int(self.speed * sec)
        if self.direction == Direction.RIGHT:
            dx = speed
        if self.direction == Direction.LEFT:
            dx = -speed
        if self.direction == Direction.UP:
            dy = -speed
        if self.direction == Direction.DOWN:
            dy = speed

        
        if not any([pygame.Rect(self.x + dx, self.y + dy, self.width, self.width).colliderect(
                pygame.Rect(tank.x, tank.y, tank.width, tank.width)) for tank in tanks if self != tank]):
            self.x, self.y = self.x + dx, self.y + dy
        self.draw()

    def print_lifes(self, coords, text=''):
        text = self.name if text == '' else text

        txt = font.render(text, True, (0,0,0))
        (x, y, w, h) = txt.get_rect()
        h += 1
        screen.blit(txt, coords)
        # print(text, x, y, w, h)
        for i in range(self.lifes):
            screen.blit(heart, (x + w + 18 + i * 26, y + coords[1]))

##########################################    Collisions    ##########################################


def checkCollisions(bullet):
    global tanks
    for i in range(len(tanks)):
        dist_x = bullet.x - tanks[i].x
        dist_y = bullet.y - tanks[i].y
        if -bullet.width <= dist_x <= tanks[i].width and -bullet.height <= dist_y <= tanks[i].width and bullet.tank != \
                tanks[i]:
            sound_col.play()
            tanks[i].lifes -= 1
            if tanks[i].lifes <= 0:
                del tanks[i]
            return True
    return False


##########################################    Init    ##########################################


mainloop = True
tank1 = Tank(700, 300, 800 // 6, 10, (3, 102, 6), 'Диана', purple_tank1, purple_tank2, fire=pygame.K_RETURN)
tank2 = Tank(100, 300, 800 // 6, 3, (135, 101, 26), 'Ера', blue_tank1, blue_tank2, pygame.K_d, pygame.K_a, pygame.K_w, pygame.K_s)
tank3 = Tank(400, 300, 800 // 6, 3, (135, 101, 26), 'Кяма',green_tank1, green_tank2, pygame.K_h, pygame.K_f, pygame.K_t, pygame.K_g, pygame.K_2)
# tank3 = Tank(100, 100, 800//6, (0, 0, 0xff), pygame.K_h, pygame.K_f, pygame.K_t, pygame.K_g, pygame.K_2)
# tank4 = Tank(100, 200, 800//6, (0xff, 255, 0), pygame.K_l, pygame.K_j, pygame.K_i, pygame.K_k, pygame.K_3)
tanks = [tank1, tank2, tank3]
bullets = []

clock = pygame.time.Clock()
FPS = 60

##########################################    Main loop    ##########################################


while mainloop:
    screen.fill((255, 255, 255))
    millis = clock.tick(FPS)
    seconds = millis / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            mainloop = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                mainloop = False

            for tank in tanks:
                if event.key == tank.fire_key:
                    bullets.append(Bullet(tank))
                if event.key in tank.KEY:
                    tank.changeDirection(tank.KEY[event.key])


    for i in range(len(tanks)):
        tanks[i].print_lifes((10, i * 43 + 10))
        # tanks[i].print_lifes((10, i * 43 + 10), f'Player {i+1}:')


    for tank in tanks:
        tank.move(seconds)

    for i in range(len(bullets)):
        bullets[i].move(seconds)
        if checkCollisions(bullets[i]) or bullets[i].lifetime > bullets[i].destroytime:
            del bullets[i]
            break

    pygame.display.flip()

pygame.quit()