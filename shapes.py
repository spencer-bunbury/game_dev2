import pygame
pygame.init()

screen = pygame.display.set_mode((600,600))
playing = True

class Circle():
    def __init__(self,color,radius,pos):
        self.screen = screen
        self.color = color
        self.radius = radius
        self.pos = pos
    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius,5)
    def grow(self):
        self.radius += 10
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius,5)

circle_1 = Circle("pink",50,(300,300))
# circle_2 = Circle("turquoise",80,(420,420))

while playing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            screen.fill("blue")
            circle_1.grow()
            pygame.display.update()
    screen.fill("blue")
    circle_1.draw()
# circle_2.draw()
    pygame.display.update()

