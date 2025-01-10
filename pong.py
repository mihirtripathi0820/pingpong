import turtle as t
import os  # To play sound

# Initialize scores
playerAscore = 0
playerBscore = 0

# Create a window and screen setup
window = t.Screen()
window.title("Pong Game with Graphics")
window.bgcolor("black")
window.setup(width=800, height=600)
window.tracer(0)

# Create the top and bottom borders for the Pong game
border = t.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.goto(-390, 290)
border.pendown()
border.pensize(3)
border.goto(390, 290)
border.goto(390, -290)
border.goto(-390, -290)
border.goto(-390, 290)

# Creating the left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5, stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Creating the right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5, stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350, 0)

# Code for creating the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ballxdirection = 0.2  # Horizontal direction of the ball
ballydirection = 0.2  # Vertical direction of the ball

# Code for creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: {}  Player B: {}".format(playerAscore, playerBscore), align="center", font=('Arial', 24, 'normal'))

# Code for moving the left paddle
def leftpaddleup():
    y = leftpaddle.ycor()
    if y < 250:  # Prevent moving out of the screen
        y += 20
    leftpaddle.sety(y)

def leftpaddledown():
    y = leftpaddle.ycor()
    if y > -240:  # Prevent moving out of the screen
        y -= 20
    leftpaddle.sety(y)

# Code for moving the right paddle
def rightpaddleup():
    y = rightpaddle.ycor()
    if y < 250:  # Prevent moving out of the screen
        y += 20
    rightpaddle.sety(y)

def rightpaddledown():
    y = rightpaddle.ycor()
    if y > -240:  # Prevent moving out of the screen
        y -= 20
    rightpaddle.sety(y)

# Assign keys to control paddles
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

# Game loop
while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # Border collision setup
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection *= -1

    # Ball hitting the right border (Player A scores)
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerAscore += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(playerAscore, playerBscore), align="center", font=('Arial', 24, 'normal'))
        os.system("afplay wallhit.wav&")  # Sound effect when ball crosses right side

    # Ball hitting the left border (Player B scores)
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ballxdirection *= -1
        playerBscore += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(playerAscore, playerBscore), align="center", font=('Arial', 24, 'normal'))
        os.system("afplay wallhit.wav&")  # Sound effect when ball crosses left side

    # Handling the collisions with paddles
    if (ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 40 and ball.ycor() > rightpaddle.ycor() - 40):
        ball.setx(340)
        ballxdirection *= -1
        os.system("afplay paddle.wav&")  # Sound effect when ball hits the right paddle

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 40 and ball.ycor() > leftpaddle.ycor() - 40):
        ball.setx(-340)
        ballxdirection *= -1
        os.system("afplay paddle.wav&")  # Sound effect when ball hits the left paddle
