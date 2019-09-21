#Case-study N1
# Developers: Arhipova A.
#             Nikitina A.
#             Revtova L.

import turtle
import math

def triangle_1(x, y, a): #blue
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(a*(math.sqrt(2)))


def triangle_3(x, y, a, b): #redNastya
        turtle.up()
        turtle.setposition(x, y)
        turtle.down()
        turtle.forward(a)
        turtle.right(135)
        turtle.forward(b)
        turtle.right(90)
        turtle.forward(b)

def triangle_4(x, y, a, b): #yellow
        turtle.up()
        turtle.setposition(x, y)
        turtle.down()
        turtle.right(180)
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(a)
        turtle.right(135)
        turtle.forward(b)

def square_1(x,y,a): #orange
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(360)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)

def triangle_5(x,y,a,b): #purple
    turtle.up()
    turtle.setposition(x,y)
    turtle.down()
    turtle.right(90)
    turtle.forward(2*a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)

def triangle_6(x, y, a):
    # TODO (Revtova.L) Draw triangle

def square_2(x, y, a):
    # TODO (Revtova.L) Draw square

def triangle_7(x, y, a, b):
    # TODO (Revtova.L) Draw triangle



def main():
        turtle.fillcolor("red")
        turtle.begin_fill()
        triangle_3(0, 0, 100, 50 * math.sqrt(2))
        turtle.end_fill()
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        triangle_4(0,0, 50 * math.sqrt(2), 100)
        turtle.end_fill()
        turtle.fillcolor("blue")
        turtle.begin_fill()
        triangle_1(100, 50, 50)
        turtle.end_fill()
        turtle.fillcolor("orange")
        turtle.begin_fill()
        square_1(50, 50, 25 * math.sqrt(2))
        turtle.end_fill()
        turtle.fillcolor("purple")
        turtle.begin_fill()
        triangle_5(50, 50, 25 * math.sqrt(2), 50)
        turtle.end_fill()
        turtle.done()

main()
