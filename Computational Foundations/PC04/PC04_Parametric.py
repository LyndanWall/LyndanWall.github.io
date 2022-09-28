'''Turtle starter code
ATLS 1300/5650
Author: Dr. Z
Author: LYNDAN WALL
DATE: 9/28/22
gradiant background gif with spirograph
'''

import turtle # import the library of commands that you'd like to use
from math import cos,sin
turtle.colormode(255) # so you can use standar RGB values, 0-255

#Create a panel to draw on. 
win =turtle.Screen()
w = 480 # width of panel
h = 480 # height of panel
win.setup(width=w, height=h) #700 x 700 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

#====================================================== Your code ======================================================

turtle.bgpic('giphy.gif')

spiro = turtle.Turtle()
spiro.hideturtle()
spiro.speed(0)
spiro.pensize(1)

R = 125 #radiant
r = 85  #radius
d = 125 #diameter

angle = 0

theta = 0.2 #spacing between each circle
steps = int(180*theta) #determines how many times the circle repeats

for t in range(0,steps):
    spiro.setheading(0)
    spiro.goto(0,-R)
    angle+=theta
    
    x = (R - r) * cos(angle)
    y = (R - r) * sin(angle)
    spiro.penup()
    spiro.goto(x,y-r)
    spiro.color("white")
    spiro.pendown()
    spiro.circle(r)
    spiro.penup()
    x = (R - r) * cos(angle) + d * cos(((R-r)/r)*angle)
    y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)

    spiro.goto(x,y)

#======= Clean up, required to run properly ======
turtle.done() # nothing should come after this line of code!