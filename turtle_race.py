import turtle
from turtle import Turtle,Screen
import random
screen=Screen()
screen.bgcolor("grey")
screen.setup(500,400)
bet=screen.textinput(title="Make Your bet",prompt="Which color turtle will win the race?")
colours=["violet","purple","blue","green","black","orange"]
t_list=[]
y=-150
for i in range(6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(-200,y=y)
    t_list.append(new_turtle)
    y+=50
game_on=True
while game_on:
    for turtle in  t_list:
        if turtle.xcor()>230:
            game_on=False
            won=turtle.pencolor()
            if bet==won:
                print(f"You Win!!!{won} turtle has won!")
            else:
                print(f"You Lost!!{won} turtle has won!!")
        distance=random.randint(0,10)
        turtle.forward(distance)
screen.exitonclick()