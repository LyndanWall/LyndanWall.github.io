#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created : October 8th, 2021

@author: Lyndan Wall

WHAT DOES YOUR CODE DO???
"""

import turtle

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 700
h = 500
panel.setup(width=w, height=h)
panel.bgcolor("black")

# ================ VARIABLE DEFINITION & SETUP =========================
#define turtle objects, variables, etc. here!
earth = turtle.Turtle(shape="circle")
size = 4
running = True
step = 1
count = 0
crosses = 10

earthImg= "earthgif.gif"
panel.addshape(earthImg)
earth.shape(earthImg)

earth.up()

# ================ FUNCTION DEFINITION =========================
# define your functions here! Use descriptive names and don't forget 
# a docstring!
def square():
    earth.color('green')
    for i in range(4):
        earth.forward(100)
        earth.right(90)
        
def circle():
    earth.color('yellow')
    for i in range(4):
        earth.circle(60)
        earth.forward(10)
        earth.right(10)

# ================ ANIMATION LOOP =========================
while running:
    earth.down()
    square()
    circle()
    earth.up()
    earth.forward(step) # move ghost
    xpos = earth.xcor() # get x position
    
    if xpos >= w/2:
        # check if it crosses the RIGHT edge
        earth.goto(-w/2,0) # move it to the left edge
        count += 1 # keep track of the crossing
        
    if count > crosses:
        # check if we've made the intened number of crosses
        running= False    
        
    panel.update() # update the window with everything drawn in a single frame
    
# CLEANUP
turtle.done()



