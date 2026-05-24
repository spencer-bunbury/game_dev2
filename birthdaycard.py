import pygame
import time

pygame.init()

screen = pygame.display.set_mode((600,600))
playing = True

image1 = pygame.image.load("images/birthday1.jpg")
image2 = pygame.image.load("images/birthday2.jpg")
image3 = pygame.image.load("images/birthday3.jpg")

font = pygame.font.SysFont("gillsansultracondensed",45)
font2 = pygame.font.SysFont("rage",55)
font3 = pygame.font.SysFont("stzhongsong",55)

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
    screen.blit(image1,(0,0))
    text1 = font.render("happy birthday",True,(0,72,54))
    screen.blit(text1,(150,150))
    pygame.display.update()
    time.sleep(4)
    screen.blit(image2,(0,0))
    text2 = font2.render("party time",True,(0,0,100))
    screen.blit(text2,(50,150))
    pygame.display.update()
    time.sleep(4)
    screen.blit(image3,(0,0))
    text3 = font3.render("open your presents",True,(0,0,100))
    screen.blit(text3,(50,150))
    pygame.display.update()
    time.sleep(4)

pygame.display.update()