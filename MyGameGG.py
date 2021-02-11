import pygame
pygame.init()
win = pygame.display.set_mode((600, 500))

pygame.display.set_caption("Game in Your ass")

WR = [pygame.image.load("Boy_walk1.png"),
      pygame.image.load("Boy_walk2.png"),
      pygame.image.load("Boy_walk3.png"),
      pygame.image.load("Boy_walk4.png"),
      pygame.image.load("Boy_walk5.png"),
      pygame.image.load("Boy_walk6.png")]


WL = [pygame.image.load("Boy_walk1L.png"),
      pygame.image.load("Boy_walk2L.png"),
      pygame.image.load("Boy_walk3L.png"),
      pygame.image.load("Boy_walk4L.png"),
      pygame.image.load("Boy_walk5L.png"),
      pygame.image.load("Boy_walk6L.png")]

PS = pygame.image.load("Boy.png")

bg = pygame.image.load("Glass.jpg")

clock = pygame.time.Clock()

x = 285
y = 285
wt = 48
ht = 48
speed = 5

ij = False
jc = 10


left = False
right = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

def DW():
    global animCount
    win.blit(bg, (0, 0))
    if animCount + 1 >= 30:
        animCount = 0
    if left:
        win.blit(WL[animCount // 5], (x, y))
        animCount +=1
    elif right:
        win.blit(WR[animCount // 5], (x, y))
        animCount +=1
    else:
        win.blit(PS, (x, y))




    pygame.display.update()

run = True
while run:
    clock.tick(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()


    if keys[pygame.K_LEFT] and x >5:
        x -=  speed
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and  x  <600 - wt - 5:
        x +=  speed
        left = False
        right = True
    elif keys[pygame.K_UP] and y > 5:
        y -= speed
        left = False
        right = True
    if keys[pygame.K_UP] and y > 5:
        if keys[pygame.K_LEFT]:
            y -= speed
            left = True
            right = False

    elif keys[pygame.K_DOWN] and y < 470:
        y += speed
        left = True
        right = False
    elif keys[pygame.K_DOWN] and [pygame.K_RIGHT]:
        right = True
        left = False
    else:
        left = False
        right = False
        animCount = 0
    if not(ij):
        if keys[pygame.K_UP] and y > 5:
            y -= speed
            left = False
            right = True
        if keys[pygame.K_DOWN] and y < 565:
            y += speed
            left = True
            right = False
        if keys[pygame.K_SPACE]:
            ij = True
    else:
        if jc >=  - 10:
            if jc <0:
                y += (jc ** 2) / 2
            else:
                y -= (jc ** 2) / 2
            jc -= 1
        else:
            ij = False
            jc = 10
    DW()






pygame.quit()



















































