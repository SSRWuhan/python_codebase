import turtle
import math

#styling the window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("ping pong")

pen = turtle.Turtle()
pen.pensize(3)
pen.pencolor("white")
pen.penup()
pen.setposition(-300, -300)
pen.pendown()
for i in range(4):
    pen.forward(600)
    pen.left(90)
pen.forward(300)
pen.left(90)
pen.dot()
pen.forward(600)

#game variables
ball_speed = 2


#creating the players

player1 = turtle.Turtle()
player1.hideturtle()
player1.penup()
player1.setposition(290, 0)
player1.shape("square")
player1.color("white")
player1.showturtle()
player1.speed(0)

player2 = turtle.Turtle()
player2.hideturtle()
player2.penup()
player2.setposition(-290, 0)
player2.shape("square")
player2.color("white")
player2.showturtle()
player2.speed(0)

#creating the ball 

ball = turtle.Turtle()
ball.penup()
ball.shape("circle")
ball.color("white")
ball.speed(0)


#game functions
def iscollition(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 20:
        return True
    else:
        return False
    
def bordrdetection(target, boder_v1, border_v2):
    if target.xcor() > boder_v1 or target.xcor() < border_v2:
        target.left(90)
    if target.ycor() > boder_v1 or target.ycor() < border_v2:
        target.left(90)


while True:
    ball.forward(ball_speed)

    bordrdetection(ball, 300, -300)

    # if iscollition(ball, player1):
    #     ball.left(180)
    # if iscollition(ball, player2):
    #     ball.left(180)