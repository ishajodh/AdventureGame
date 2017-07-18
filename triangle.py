from turtle import *
import math
TimTed = Turtle ()
#timted position
setup (500,300)
x_pos = 0
y_pos = 0
TimTed.penup()
TimTed.setposition(x_pos, y_pos)
#Draw the shape
TimTed.fillcolor("magenta")
TimTed.begin_fill()
TimTed.pendown()
TimTed.pencolor("blue1")
TimTed.speed("slow")
#loop for triangle
counter=9
for times in range (1,9):
    #print(TimTed)
    TimTed.forward(100)
    TimTed.left(120)
TimTed.end_fill()
exitonclick()
