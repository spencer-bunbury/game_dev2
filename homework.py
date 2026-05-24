import pgzrun

WIDTH = 800
HEIGHT = 500

GRAVITY = 2000.0

class Ball():
    def __init__(self,x,y,r,color):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 200
        self.vy = 0
        self.color = color
    def display(self):
        screen.draw.filled_circle((self.x,self.y),self.r,self.color)

ball_1 = Ball(250,400,30,"light blue")
ball_2 = Ball(160,400,30,"light pink")
ball_3 = Ball(370,400,30,"blue")

balls = [ball_1,ball_2,ball_3]

def draw():
    screen.fill("black")
    ball_1.display()
    ball_2.display()
    ball_3.display()

def update(dt):
    uy = ball_1.vy
    ball_1.vy += GRAVITY*dt
    ball_1.y += (uy + ball_1.vy)*0.5*dt
    if ball_1.y >= 500:
        ball_1.y = 500
        ball_1.vy = -ball_1.vy*0.9
    ball_1.x += ball_1.vx*dt
    if ball_1.x >= 800 or ball_1.x <= 0:
        ball_1.vx = -ball_1.vx
        uy = ball_1.vy
    ball_2.vy += GRAVITY*dt
    ball_2.y += (uy + ball_2.vy)*0.5*dt
    if ball_2.y >= 500:
        ball_2.y = 500
        ball_2.vy = -ball_2.vy*0.9
    ball_2.x += ball_2.vx*dt
    if ball_2.x >= 800 or ball_2.x <= 0:
        ball_2.vx = -ball_2.vx
        uy = ball_3.vy
    ball_3.vy += GRAVITY*dt
    ball_3.y += (uy + ball_3.vy)*0.5*dt
    if ball_3.y >= 500:
        ball_3.y = 500
        ball_3.vy = -ball_3.vy*0.9
    ball_3.x += ball_3.vx*dt
    if ball_3.x >= 800 or ball_3.x <= 0:
        ball_3.vx = -ball_3.vx

def on_key_down(key):
    if key == keys.UP:
        ball_1.vy = -1000
    if key == keys.D:
        ball_2.vy = -1000
    if key == keys.C:
        ball_3.vy = -1000
    if key == keys.DOWN:
        ball_1.vy = +1000
    if key == keys.B:
        ball_2.vy = +1000
    if key == keys.A:
        ball_3.vy = +1000
pgzrun.go()