from turtle import Turtle, Screen
import turtle
import random
niki=Turtle()
turtle.colormode(255)
def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    colour=(r,g,b)
    return colour
niki.speed(0)
def draw_spiro(size_of_gap):
    for i in range(360//size_of_gap):
        niki.color(random_color())
        niki.circle(100)
        niki.setheading(niki.heading()+size_of_gap)
draw_spiro(5)




































screen= Screen()
screen.exitonclick()