from turtle import Turtle, Screen
import turtle
import random
joey=Turtle()
directions=[0,90,180,270]
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colour=(r,g,b)
    return colour
joey.pensize(10)
joey.speed(10)
for i in range(200):
    joey.forward(30)
    joey.color(random_color())
    joey.setheading(random.choice(directions))




























screen= Screen()
screen.exitonclick()
