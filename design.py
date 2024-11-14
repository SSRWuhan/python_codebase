import turtle

turtle.bgcolor("black")

pen = turtle.Turtle()

colors = ["red", "blue"]
pen.speed(0)
length = 1

while True:
    for i in range(4):
        length += 1
        pen.pendown()
        pen.pencolor(colors[((i+1)%2)])
        pen.forward(length)
        # pen.left(39)
        # pen.left(100)
        pen.left(200)
