import pgzrun

WIDTH = 800
HEIGHT = 500

GRAVITY = 2000.0

class Ball():
    def __init__(self,x,y,r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 200
        self.vy = 0
    def display(self):
        screen.draw.filled_circle((self.x,self.y),self.r,"light blue")

ball_1 = Ball(250,400,30)

def draw():
    screen.fill("black")
    ball_1.display()

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

def on_key_down(key):
    if key == keys.SPACE:
        ball_1.vy = -1000
pgzrun.go()