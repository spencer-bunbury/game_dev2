import pygame
from pygame.locals import*
from random import*
import time

pygame.init()
pygame.font.init()
pygame.mixer.init()

screen = pygame.display.set_mode((900,500))
playing = True

font1 = pygame.font.SysFont("rage",45)
font = pygame.font.SysFont("gillsansultracondensed",45)

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

lives = 3
lives2 = 3

rb = []
lb = []

def hb():
    global lives,lives2
    for r in rb:
        r.x -= 5
        if r.colliderect(lpp):
            lives -= 1
            rb.remove(bullet)
    for l in lb:
        l.x += 5
        if l.colliderect(rpp):
            lives2 -= 1
            lb.remove(bullet)
while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                bullet = pygame.Rect(rpp.x,rpp.y + 15,10,7)
                rb.append(bullet)
            if event.key == pygame.K_x:
                bullet = pygame.Rect(lpp.x,lpp.y + 15,10,7)
                lb.append(bullet)
            if event.key == K_UP:
                rpp.y -= 40
            if event.key == K_LEFT and rpp.x >= 485:
                rpp.x -= 40
            if event.key == K_RIGHT:
                rpp.x += 40
            if event.key == K_DOWN:
                rpp.y += 40
            if event.key == K_w:
                lpp.y -= 40
            if event.key == K_a:
                lpp.x -= 40
            if event.key == K_d and lpp.x <= 400:
                lpp.x += 40
            if event.key == K_s:
                lpp.y += 40
            if lives == 1:
                screen.fill("black")
                text1 = font.render("right player wins",True,"pink")
                screen.blit(text1,(350,250))
                pygame.display.update()
                time.sleep(5)
                playing = False
            elif lives2 == 1:
                screen.fill("black")
                text2 = font.render("left player wins",True,"pink")
                screen.blit(text2,(350,250))
                pygame.display.update()
                time.sleep(5)
                playing = False
    screen.blit(bg,(0,0))
    screen.blit(lp,(lpp.x,lpp.y))
    screen.blit(rp,(rpp.x,rpp.y))
    text = font1.render("lives = " + str(lives),True,"pink")
    text2 = font1.render("lives = " + str(lives2),True,"pink")
    screen.blit(text,(50,50))
    screen.blit(text2,(600,50))

    pygame.draw.rect(screen,"black",pygame.Rect(450,0,20,500))
    for r in rb:
        pygame.draw.rect(screen,"yellow",r)
    for l in lb:
        pygame.draw.rect(screen,"red",l)
    hb()
    pygame.display.update()