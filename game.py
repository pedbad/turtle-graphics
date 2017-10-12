#Turtle Graphics Game
#python 2.7.12 on Mac
# Thanks to Christian Thompson 
# Python Game Programming Tutorial: Space Invaders
# http://christianthompson.com/

import turtle

#Set up the screen

win = turtle.Screen()
win.bgcolor("lawngreen")
win.title("Turtle Game")

#Create player turtle
player = turtle.Turtle()
player.speed(0)
player.color("blue")
player.shape("turtle")
player.penup()

#Set speed variable
speed = 1



#Define functions here

def turnLeft():
  player.left(30)


def turnRight():
  player.right(30)

#Set up keyboard bindings
turtle.listen()
turtle.onkey(turnLeft, "Left")
turtle.onkey(turnRight, "Right")

#forever loop
while True:
  player.fd(speed)







#delay = raw_input("Press enter to finish.")