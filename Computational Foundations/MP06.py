#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: lyndanwall
"""

import turtle

turtle.colormode(255)

panel=turtle.Screen()
w=600
h=600
panel.setup(width=w,height=h)

class CLASSNAME:
    def _init_(self, placeholder, location):
        self.turtle1=turtle.Turtle()
        self.turtle1.color(placeholder)
        self.turtle1.shape('square')
        self.turtle1.goto(location)
    def colorChange(self):
        self.turtle1.color('red')
        
        
placeholderval = 'yellow'
location1=(100,100)
object1=CLASSNAME(placeholderval,location1)

object2=CLASSNAME('red',(200,200))
