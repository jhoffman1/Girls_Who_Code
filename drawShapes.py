from turtle import *
import math


# Name your Turtle.
t = Turtle()


def drawShape(numSides):
    angle = 360/numSides

    for x in range(numSides):
        t.forward(25)
        t.right(angle)
    #print(angle)

def checkforexit(ipt):
    if ipt == "exit":
        print("Bye")
        exit()

# Set Up your screen and starting position.
setup(500,500)
#x_pos = -250
#y_pos = -150
#t.setposition(x_pos, y_pos)

### Write your code below:
exit = 0
t.penup()
t.setposition(-200,200)

while exit == 0:
    t.pendown()
    print("Input the number of sides on the shape")
    sides = input()
    checkforexit(sides)
    sides = int(sides)

    print("Input the color of the shape")
    checkforexit(sides)
    color = input()

    t.color(color)
    t.pencolor(color)
    drawShape(sides)

    t.penup()

    print("Would you like to draw another shape?")
    print("Type 'yes' or 'no'")
    user_input3 = input()

    if user_input3 == 'no':
        exit = 1
    else:
        t.forward(75)
        t.right(90)
        t.forward(75)
        t.left(90)

#exit()


# Close window on click.
exitonclick()
