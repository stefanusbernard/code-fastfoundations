import sys
import turtle


def draw_rectangle():
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(10)


def draw_circle():
    pen = turtle.Turtle()
    if pen.isdown():
        pen.up()
    pen.goto(15, 28)
    pen.down()
    pen.begin_fill()
    pen.pencolor("red")
    pen.fillcolor("purple")
    pen.circle(60)
    pen.end_fill()
    pen.up()


def main():
    draw_rectangle()
    draw_circle()
    turtle.done()
    return 0


if __name__ == "__main__":
    sys.exit(main())
