#Case-study N1
# Developers: Arhipova A.
#             Nikitina A.
#             Revtova L.


import turtle
import math

def square_2(x,y,a):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(135)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)

def parallelogram_1(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.right(45)
    turtle.forward(b)


def triangle_3(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(b)

def triangle_3(x, y, a, b):
        turtle.up()
        turtle.setposition(x, y)
        turtle.down()
        turtle.right(45)
        turtle.forward(a)
        turtle.right(135)
        turtle.forward(b)
        turtle.right(90)
        turtle.forward(b)

def triangle_3(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(b)

def triangle_3(x, y, a, b):
        turtle.up()
        turtle.setposition(x, y)
        turtle.down()
        turtle.right(45)
        turtle.forward(a)
        turtle.right(135)
        turtle.forward(b)
        turtle.right(90)
        turtle.forward(b)


def triangle_3(x, y, a, b):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.right(45)
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(90)
    turtle.forward(b)

def main():
    turtle.fillcolor("orange")
    turtle.begin_fill()
    turtle.right(90)
    square_2(50, 340, 25*math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("green")
    turtle.begin_fill()
    parallelogram_1(40, 340, 50, 25 * math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(270)
    triangle_3(110,340, 100, 50 * math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.left(90)
    triangle_3(0, 230, 100, 50 * math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.left(90)
    triangle_3(5, 235, 50, 25 * math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.left(135)
    triangle_3(70, 190, 80, 40 * math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("pink")
    turtle.begin_fill()
    turtle.left(90)
    triangle_3(70, 210, 50, 25 * math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("purple")
    turtle.begin_fill()
    turtle.right(90)
    square_2(200, 340, 25 * math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(90)
    triangle_3(200, 340, 100, 50 * math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("orange")
    turtle.begin_fill()
    turtle.left(90)
    triangle_3(300, 240, 100, 50 * math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("blue")
    turtle.begin_fill()
    turtle.left(90)
    turtle.fillcolor("pink")
    turtle.begin_fill()
    parallelogram_1(300, 311, 50, 25 * math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("black")
    turtle.begin_fill()
    triangle_3(300, 215, 60, 30 * math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.left(135)
    triangle_3(0, 0, 0, 0)
    turtle.end_fill()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(90)
    triangle_3(300, 200, 50, 25 * math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("black")
    turtle.begin_fill()
    parallelogram_1(210, 270, 50, 25 * math.sqrt(2))
    turtle.end_fill()
    turtle.fillcolor("red")
    turtle.begin_fill()
    turtle.left(90)
    triangle_3(200, 350, 40, 20 * math.sqrt(2))
    turtle.end_fill()

    turtle.done()



main()


