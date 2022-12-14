#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on WHAT DAY IS IT?

@author:  Lyndan Wall

WHAT DOES YOUR GAME DO?
    OBJECTIVE - Turn all the boxes into the same color
    RULES - No rules just a fun little game
    CHALLENGE - Click on all the boxes until they turn the same color
    INTERACTIONS - Click interactions

"""

import turtle
import time, random

# ================ LIBRARY SETTINGS SETUP =========================
turtle.colormode(255) # accept 0-255 RGB values
turtle.tracer(0) # turn off turtle's animation

panel = turtle.Screen()
w = 800
h = 800
panel.setup(width=w, height=h)
panel.bgcolor('black')
#set up images for game

# ================ VARIABLE DEFINITION & SETUP =========================
running = True

# ================ FUNCTION DEFINITION =========================
# functions should go here IF they work with objects. 
# otherwise, try to include them in classes 

# ================Countdown Class=========================
def countdown (t) :
    global running
    if t>0:  
        mins, secs = divmod(t, 1)
        timer = '{:02d}'.format(mins)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1
    else:
        running=False
      
    print(' Ready, Set, Begin!')
  
# input time in seconds
t = 10
print(t)
  
# function call
countdown(t)

# ================ CLASSES =========================
class Button:
    def __init__(self, placeholder, location):
        self.rainbow = turtle.Turtle()
        self.rainbow.color(placeholder)
        self.rainbow.shape('square')
        self.rainbow.shapesize(6,6,1)
        self.rainbow.up()
        self.rainbow.goto(location)
        self.rainbow.onclick(self.colorChange)
        
    def colorChange(self,x,y):
        
        self.rainbow.color('black')
        
# ================ OBJECTS =========================
# instantiate objects here

def run():
    instanceList = turtle("black", random.randint(-300,300))
    
    instanceList = []
    X = random.randint(-300,300)
    C = random.choice(turtle.colors)
    instanceList.append(turtle(C,X))
 
top1sq= 116,0,184 
location1=(-300,200)
object1=Button(top1sq,location1)

top2sq= 105,48,195
location2=(-100,200)
object2= Button(top2sq,location2)

top3sq = 94,96,206
location3=(100,200)
object3= Button(top3sq,location3)

top4sq = 83,144,217
location4 = (300,200)
object4= Button(top4sq,location4)

middle1sq= 78,168,222
location5=(-300,0)
object5=Button(middle1sq,location5)

middle2sq= 72,191,227
location6=(-100,0)
object6= Button(middle2sq,location6)

middle3sq = 86,207,225
location7=(100,0)
object7= Button(middle3sq,location7)

middle4sq = 100,223,223
location8 = (300,0)
object8= Button(middle4sq,location8)

bottom1sq= 114,239,221
location9=(-300,-200)
object9=Button(bottom1sq,location9)

bottom2sq= 128,255,219
location10=(-100,-200)
object10= Button(bottom2sq,location10)

bottom3sq = 170,255,228
location11=(100,-200)
object11= Button(bottom3sq,location11)

bottom4sq = 191,255,250
location12 = (300,-200)
object12= Button(bottom4sq,location12)

# ================ ANIMATION LOOP =========================
# PRO-MOVES - can you get this while loop into a class? 
# You will have to for PC09.

while running:

    objList = [object1, object2, object3, object4, object5, object6, object7, object8, object9, object10, object11, object12]
    
    def checkColor(objList):
        for rainbow in objList:
            if rainbow.color()['black'] != rainbow.targetColor: 'black'
            return
        else: rainbow.color('White') 
        style = ('Arial', 50, 'italic') 
        rainbow.write('Thanks for Playing!', font=style, align='center') 
        rainbow.hideturtle()
    

    panel.update() # update the window with everything drawn in a single frame
    
# ================ CLEANUP =========================
turtle.mainloop()  # allows for user interactions; handles cleanup


run()
