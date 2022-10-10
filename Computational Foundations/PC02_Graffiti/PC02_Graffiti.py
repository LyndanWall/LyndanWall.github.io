'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Lyndan Wall
DATE: 9/14/22
REVISED DATE: 10/10/22
DESCRIPTION: 
Using Ada Lovelace as my background, I drew a circle, square, and line on top of her using turtle. 
You must make sure all images you reference in the code is in the same folder as this script!
'''

import turtle #import the library of commands that you'd like to use
turtle.speed(0) #turns off animation so code shows up all at once
turtle.colormode(255)

# Create a panel to draw on. 
win = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
win.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Ada's image to it
win.bgcolor("seashell4")
bgImg = "./FullAda_Glam.gif"
stampImg = "./JustAda_Glam.gif"
win.addshape(stampImg) # Now you can use Ada's image as a stamp. USE THE DOCS.

win.bgpic(bgImg) # sets the background to the selected image.
#Comment out the line above to remove the image from background

#=======Add your code here======

# drawing turtle green circle shape
turtle.color((113,139,90))
turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()

# compete circle and prep code to move to another shape
turtle.penup()

# moving turtle to different location
turtle.goto(0,-160)
turtle.pendown()

# drawing turtle blue diamolnd/square shape
turtle.color("#4DA6FF")
turtle.circle(80,steps=4)

# complete square and prep code to move to another shape
turtle.penup()

# moving turtle to different location
turtle.goto(0,160)
turtle.pendown()

# drawing turtle line with thicker line weight
turtle.color((77,165,255))
turtle.pensize(4)

# coding direction of arrow
turtle.forward(80)

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()

# Critisism sandwich:
# positive: code works well without errors
# negative: artistically, I could have thought through my process more in depth, 
# My code descriptions also could have been more in depth
# positive: I think the colors are complementary to Ada Lovelace's dress (purple)
