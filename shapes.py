from turtle import Turtle, Screen
import random
colours=["red","blue","bisque3","chartreuse","cyan3","DarkGreen","DarkGray","DarkRed"]
niki = Turtle()
niki.shape("classic")
def shape(sides):
    angle=360/sides
    for i in range(sides):
        niki.forward(100)
        niki.right(angle)
for number in range(3,11):
    niki.color(colours[number - 3])
    shape(number)


























'''
for i in range (3):
    niki.color("violet")
    niki.forward(100)
    niki.right(120)
for i in range (4):
    niki.color("bisque4")
    niki.forward(100)
    niki.right(90)
for i in range (5):
    niki.color("blue")
    niki.forward(100)
    niki.right(72)
for i in range(6):
    niki.color("yellow")
    niki.forward(100)
    niki.right(60)
for i in range(7):
    niki.color("orange")
    niki.forward(100)
    niki.right(51.4285714)
for i in range(8):
    niki.color("red")
    niki.forward(100)
    niki.right(45)
for i in range(9):
    niki.color("grey")
    niki.forward(100)
    niki.right(40)
for i in range(10):
    niki.color("brown")
    niki.forward(100)
    niki.right(36)
'''














screen= Screen()
screen.exitonclick()