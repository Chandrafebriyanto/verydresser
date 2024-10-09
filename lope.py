import turtle
import time

screen = turtle.Screen()
screen.setup(800, 600)
screen.bgcolor("pink")
# time.sleep(1)

t = turtle.Turtle()
t.hideturtle()
t.speed(2)

def hati(x, y, size, color, thickness):
    t.penup()
    t.goto(x, y)
    t.color(color)
    t.pensize(thickness)
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(size)
    
    for _ in range(200):
        t.right(1)
        t.forward(size*0.009)
        
    t.left(120)    
        
    for _ in range(201):
        t.right(1)
        t.forward(size*0.009)
        
    t.forward(size)
    t.end_fill()
    t.setheading(0)
    
heart = [
    (0, -180, 300, "#ff9999", 5),
    (0, -165, 270, "#ffcccc", 5),
    (0, -150, 240, "#ff99cc", 5),
    (0, -135, 210, "#ffccff", 5),
    # (0, -120, 180, "#ff6666", 5),
    # (0, -105, 150, "#ff9999", 5),
    # (0, -90, 120, "#ff6666", 5)
]

for heart in heart:
    hati(*heart)
    time.sleep(2)