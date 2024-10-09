import math
import turtle

turtle.bgcolor("pink")
turtle.pencolor("black")
turtle.shape("triangle")
turtle.speed(0)
turtle.fillcolor("orange")
pi = 137.508*(math.pi/180.0)

for i in range (180 +20):
    r = 4*math.sqrt(i)
    tan = i*pi
    x = r*math.cos(tan)
    y = r*math.sin(tan)
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(i*137.508)
    turtle.pendown()
    if i < 160:
        turtle.stamp()
    else:
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        turtle.left(-5)
        turtle.circle(500, 25)
        turtle.right(-155)
        turtle.circle(500, 25)
        turtle.end_fill()
turtle.hideturtle()
turtle.done()

