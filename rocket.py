import pygame
from pygame.locals import*
from time import*

playing = True
pygame.init()
screen = pygame.display.set_mode((600,600))

x = 250
y = 100

font1 = pygame.font.SysFont("rage",55)
text1 = font1.render("YOU LOST",True,"pink")

image1 = pygame.image.load("images/SPACE.png")
image2 = pygame.image.load("images/rocket.png")

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == K_UP:
                y -= 50
            if event.key == K_LEFT:
                x -= 20
            if event.key == K_RIGHT:
                x += 20
    y  += 20
    screen.blit(image1,(0,0))
    screen.blit(image2,(x,y))
    if y >= 570:
        screen.fill("blue")
        screen.blit(text1,(230,300))
        pygame.display.update()
    sleep(0.1)
    pygame.display.update()