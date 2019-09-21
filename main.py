#Case-study N1
# Developers: Arhipova A.
#             Nikitina A.
#             Revtova L.

import turtle
import math

def triangle_3(x, y, a, b): #redNastya
        turtle.up()
        turtle.setposition(x, y)
        turtle.down()
        turtle.forward(a)
        turtle.right(135)
        turtle.forward(b)
        turtle.right(90)
        turtle.forward(b)

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
    right(360)
    forward(a)
    right(90)
    forward(a)
    right(90)
    forward(a)
    right(90)
    forward(a)

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
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(45)

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

def main():
        turtle.fillcolor("red")
        turtle.begin_fill()
        triangle_3(0, 0, 100, 50 * math.sqrt(2))
        turtle.end_fill()
        turtle.fillcolor("yellow")
        turtle.begin_fill()
        triangle_4(0,0, 50 * math.sqrt(2), 100)
        turtle.end_fill()
        turtle.done()
    #ALENA NIKITINA DEF MAIN
    #turtle.fillcolor('green')
    #turtle.begin_fill()
    #parallelogram_2(25, 75, 50, 25 * math.sqrt(2))
    #turtle.end_fill()
    #turtle.left(45)
    #turtle.fillcolor("pink")
    #turtle.begin_fill()
    #triangle_2(25, 75, 25 * math.sqrt(2), 50)
    #turtle.end_fill()

    #LIDA REVTOVA DEF MAIN
#fillcolor("blue")
#begin_fill()
#triangle_1(100, 50, 50)
#end_fill()
#fillcolor("orange")
#begin_fill()
#square_1(50, 50, 25 * math.sqrt(2))
#end_fill()
#fillcolor("purple")
#begin_fill()
#triangle_5(50, 50, 25 * math.sqrt(2), 50)
#end_fill()
#turtle.done()
main()
