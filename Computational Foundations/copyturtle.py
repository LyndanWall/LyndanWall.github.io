
# author: Lyndan Wall
# ATLS 1300
# date: Sep. 8th 2022
# Description:

import turtle

panel = turtle.Screen()
w = 700
h = 700
panel.setup(width=w, height=h)

turtle.colormode(255)

ellipse = turtle.Turtle()
ellipse.color('orange')

scale= 10
radiusX = 10
radiusY= 5

ellipse.begin_fill()
for angle in range(50):
    ellipse.goto(0.0)
ellipse.end_fill()

arms = turtle.Turtle()
arms.color('periwinkle')
arms.penwidth(10)
arms.up()

turtle.done()