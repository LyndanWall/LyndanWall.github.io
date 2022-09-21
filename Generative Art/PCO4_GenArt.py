#PCO3 Generative Art
#Author: Lyndan Wall
#Date: September 21st, 2022

#DESCRIPTION: infinate squares follow random color pattern while growin gin size

import turtle, random

turtle.colormode(255)

#creating panel
panel = turtle.Screen()
w = 600
h = 600
panel.setup(width=w,height=h)

#======CODE=======#

#using the random function on colors
colorList = [(178,132,190),(176,191,26),(124,185,232),(229,43,80),(255,126,0),(239,222,205)]

turtle.speed(0)

turtle.goto(-300,-300)

turtle.penup()

#drawing the infinate squares
def draw_square(size):
    turtle.pendown()
    turtle.color(random.choice(colorList))   #using random function
    for i in range(4):
        turtle.forward(size)
        turtle.left(90)
    turtle.penup()

#conditional
for i in range(600):
    if i % 2 == 0:
        draw_square(i)




