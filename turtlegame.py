import turtle
import math
import random

#setting the screen color
wn = turtle.Screen()
wn.bgcolor("black")
wn.tracer(3)
wn.title("turtle graphics game")

#creating border
pen = turtle.Turtle()
pen.penup()
pen.setposition(-300, -300)
pen.pendown()
pen.color("white")
pen.pensize(3)
for i in range(4):
    pen.forward(600)
    pen.left(90)
pen.hideturtle()

#creating player
player = turtle.Turtle()
player.shape("triangle")
player.color("blue")
player.speed(0)
player.penup()
#player speed
speed = 1

#creating variable to keep track oof score
score = 0

#player control functions
def turnleft():
    player.left(30)

def turnright():
    player.right(30)

def speedup():
    global speed
    speed += 1

#Note: uncomment the first if statement and comment line 49 and 52 to 54 if you want to get rid of the slow down cost
def speeddown():
    global speed
    # global score
    if speed > 0:
        speed -= 1
    # if score > 0 and speed > 0:
        # score -= 5
        # speed -=1

#game functions
def iscollition(t1, t2):
    distance = math.sqrt(math.pow(t1.xcor() - t2.xcor(), 2) + math.pow(t1.ycor() - t2.ycor(), 2))
    if distance < 20:
        return True
    else:
        return False
    
def bordrdetection(target, boder_v1, border_v2):
    if target.xcor() > boder_v1 or target.xcor() < border_v2:
        target.left(180)
    if target.ycor() > boder_v1 or target.ycor() < border_v2:
        target.left(180)

#creating goal
max_goals = 10
goals = []

for i in range(max_goals):
    goals.append(turtle.Turtle())
    goals[i].shape("circle")
    goals[i].color("red")
    goals[i].penup()
    goals[i].setposition(random.randint(-300, 300),random.randint(-300, 300))
    goals[i].speed(0)

#keyboard bindings
#for single press settings
turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(speedup, "Up")
turtle.onkey(speeddown, "Down")
#for long press settings
# turtle.listen()
# turtle.onkeypress(turnleft, "Left")
# turtle.onkeypress(turnright, "Right")
# turtle.onkeypress(speedup, "Up")
# turtle.onkeypress(speeddown, "Down")


#game loop
while True:
    player.forward(speed)

    bordrdetection(player, 300, -300)
    
    for i in range(max_goals):
        goals[i].forward(3)
        bordrdetection(goals[i], 290, -290)

        #collison detection
        if iscollition(player, goals[i]):
            goals[i].hideturtle()
            goals[i].setposition(random.randint(-300, 300),random.randint(-300, 300))
            goals[i].showturtle()
            goals[i].right(random.randint(-300, 300))
            score += 1
            #printing the score on the board
            pen.undo()
            pen.penup()
            pen.hideturtle()
            pen.setposition(-290, 300)
            stringscore = "score: " + str(score)
            pen.write(stringscore, False, align="left", font=("Arial", 14, "normal"))

