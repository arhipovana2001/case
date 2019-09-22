#Case-study N1
# Developers: Arhipova A.
#             Nikitina A.
#             Revtova L.

import turtle
import math
from turtle import *

def triangle_3(x, y, a, b): #redNastya
    up()
    setposition(x, y)
    down()
    right(45)
    forward(a)
    right(135)
    forward(b)
    right(90)
    forward(b)

def triangle_4(x, y, a, b): #yellowNastya
        turtle.up()
        turtle.setposition(x, y)
        turtle.down()
        turtle.right(180)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a)
        turtle.right(135)
        turtle.forward(b)



def triangle_6(x, y, a):
    # TODO (Revtova.L) Draw triangle
    up()
    setposition(x, y)
    down()
    right(90)
    forward(a)
    right(90)
    forward(a)
    right(135)
    forward(a * (math.sqrt(2)))

def square_2(x, y, a):
    # TODO (Revtova.L) Draw square
    up()
    setposition(x, y)
    down()
    right(135)
    fd(a)
    right(90)
    fd(a)
    right(90)
    fd(a)
    right(90)
    fd(a)

def triangle_7(x, y, a, b):
    # TODO (Revtova.L) Draw triangle
    up()
    setposition(x, y)
    down()
    right(90)
    forward(2 * a)
    right(135)
    forward(b)
    right(135)
    forward(a)

def parallelogram_1(x, y, a, b):
    # TODO (Nikitina.A) Draw parallelogram
    up()
    setposition(x, y)
    down()
    fd(a)
    right(45)
    fd(b)
    right(135)
    fd(a)
    right(45)
    fd(b)

def triangle_8(x, y, a, b):
    # TODO (Nikitina.A) Draw triangle
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(90)

def rabbit():
    fillcolor("green")
    begin_fill()
    parallelogram_1(0,0,25*math.sqrt(2),50)
    end_fill()
    fillcolor("orange")
    begin_fill()
    square_2(37.5*math.sqrt(2),-25*math.sqrt(2),25*math.sqrt(2))
    end_fill()
    fillcolor("red")
    begin_fill()
    triangle_3(-50*math.sqrt(2)/4,-87.5*math.sqrt(2),100,50*math.sqrt(2))
    end_fill()
    fillcolor("purple")
    begin_fill()
    triangle_3(25*math.sqrt(2),50/3*2-137.5*math.sqrt(2),-50,-25*math.sqrt(2))
    end_fill()
    fillcolor("blue")
    begin_fill()
    triangle_3(-46.66*math.sqrt(2)/4,-137.5 *math.sqrt(2),-50*math.sqrt(2),-50)
    end_fill()
    fillcolor("yellow")
    begin_fill()
    right(90)
    triangle_3(37.5*math.sqrt(2),-87.5*math.sqrt(2),100,50 * math.sqrt(2))
    end_fill()
    fillcolor("pink")
    begin_fill()
    right(225)
    triangle_3(37.5 * math.sqrt(2),-87.5*math.sqrt(2)-50*math.sqrt(2)/3,50,25*math.sqrt(2))
    end_fill()
rabbit()

def fish():
    fillcolor("red")
    begin_fill()
    right(45)
    triangle_3(-200,0,100, 50 * math.sqrt(2))
    end_fill()
    fillcolor("orange")
    begin_fill()
    right(90)
    square_2(-200-50*math.sqrt(2)/3*2,0, 25*math.sqrt(2))
    end_fill()
    fillcolor("yellow")
    begin_fill()
    right(45)
    triangle_3(-200-50*math.sqrt(2),-50*math.sqrt(2), 100, 50 * math.sqrt(2))
    end_fill()
    fillcolor("blue")
    begin_fill()
    right(45)
    triangle_3(-200,-25,50 * math.sqrt(2),50)
    end_fill()
    fillcolor("green")
    begin_fill()
    right(45)
    parallelogram_1(-200-50*math.sqrt(2)/3*2,0,25 * math.sqrt(2),50)
    end_fill()
    fillcolor("pink")
    begin_fill()
    right(45)
    triangle_3(-200-50*math.sqrt(2)/3*2,0, 50,25*math.sqrt(2))
    end_fill()
    fillcolor("purple")
    begin_fill()
    right(270)
    triangle_3(-247-50* math.sqrt(2),-25* math.sqrt(2),50,25 *math.sqrt(2))
    end_fill()
    done()

fish()








