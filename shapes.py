import turtle


def star(x, y, size):
    turtle.penup()
    turtle.goto((x, y))
    turtle.setheading(0)
    turtle.pendown()
    for i in range(5):
        turtle.forward(size)
        turtle.right(180 - (180 / 5))