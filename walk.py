from turtle import Turtle, Screen
import turtle
import random
niki=Turtle()
directions=[0,90,180,270]
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colour=(r,g,b)
    return colour
niki.pensize(10)
niki.speed(10)
for i in range(200):
    niki.forward(30)
    niki.color(random_color())
    niki.setheading(random.choice(directions))




























screen= Screen()
screen.exitonclick()