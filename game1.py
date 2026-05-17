import pygame
from random import randint

pygame.init()

screen = pygame.display.set_mode((800,500))
playing = True

class bird():
    def __init__(self,color,x,y,width,height):
        self.screen = screen
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def forward(self):
        self.x += 10
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height))
    def backward(self):
        self.x -= 10
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height))
    def draw(self):
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height))

class enemy():
    def __init__(self,color,x,y,width,height):
          self.screen = screen
          self.color = color
          self.x = x
          self.y = y
          self.width = width
          self.height = height
    def going_down(self):
        if self.y != 9:
            self.y += 10
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height))
    def draw(self):
        pygame.draw.rect(self.screen,self.color,(self.x,self.y,self.width,self.height))

flappy_bird = bird("pink",30,400,40,40)
enemy_1 = enemy("white",randint(20,780),0,5,6)

i = True

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
            while i == True:
                enemy_1.going_down()
                pygame.display.update()
            if event.type == pygame.K_LEFT:
                flappy_bird.forward()
                pygame.display.update()
            if event.type == pygame.K_RIGHT:
                flappy_bird.backward()
                pygame.display.update()
        screen.fill("blue")
        enemy_1.draw()
        flappy_bird.draw()
    pygame.display.update()