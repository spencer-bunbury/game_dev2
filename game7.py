import pygame
from pygame.locals import*
from random import*

pygame.init()
pygame.font.init()
pygame.mixer.init()

screen = pygame.display.set_mode((900,500))
playing = True

bg = pygame.image.load("images/space2.png")
lp = pygame.image.load("images/rocket2.png")
lp = pygame.transform.scale(lp,(55,40))
lp = pygame.transform.rotate(lp,90)
rp = pygame.image.load("images/rocket3.png")
rp = pygame.transform.scale(rp,(55,40))
rp = pygame.transform.rotate(rp,270)

s1 = pygame.mixer.Sound("images/g.mp3")
s2 = pygame.mixer.Sound("images/g2.mp3")

lpp = pygame.Rect(250,250,50,50)
rpp = pygame.Rect(650,250,50,50)

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit() 
    screen.blit(bg,(0,0))
    screen.blit(lp,(lpp.x,lpp.y))
    screen.blit(rp,(rpp.x,rpp.y))
    pygame.draw.rect(screen,"black",pygame.Rect(450,0,20,500))

    pygame.display.update()