import turtle
import os
import time
import random

furtherPlay = True

win = turtle.Screen()
win.title('Pong')
win.bgcolor('black')
win.setup(width=800, height=600)
win.tracer(0)

# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape('square')
paddleA.color('white')
paddleA.penup()
paddleA.goto(-350, 0)
paddleA.shapesize(stretch_wid=5, stretch_len=1, outline=None)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape('square')
paddleB.color('white')
paddleB.penup()
paddleB.goto(350, 0)
paddleB.shapesize(stretch_wid=5, stretch_len=1, outline=None)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)
ball.dx = 0.025 + random.random()/10
ball.dy = 0.025 + random.random()/10
print(ball.dx, ball.dy)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0  Player B: 0', align='center', font=('Courier', 24, 'normal'))

# Scores
scoreA = 0
scoreB = 0

# Functions
def paddleAUp():
    y = paddleA.ycor()
    if y <= 240:
        paddleA.sety(y+10)

def paddleADown():
    y = paddleA.ycor()
    if y >= -240:
        paddleA.sety(y-10)

def paddleBUp():
    y = paddleB.ycor()
    if y <= 240:
        paddleB.sety(y+10)

def paddleBDown():
    y = paddleB.ycor()
    if y >= -240:
        paddleB.sety(y-10)


def endGame(win):
    ball.hideturtle()
    pen.goto(0, 0)
    pen.write('Player {} Won!'.format(win), align='center', font=('Courier', 24, 'normal'))
    time.sleep(2.5)


# Keyboard binding
win.listen()
win.onkeypress(paddleAUp, 'w')
win.onkeypress(paddleADown, 's')
win.onkeypress(paddleBUp, 'Up')
win.onkeypress(paddleBDown, 'Down')

# Main Loop
while furtherPlay == True:
    win.update()

    # Moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Check
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
        os.system('aplay bounce.wav&')
        
    if ball.xcor() > 390 or ball.xcor() < -390:
        if ball.xcor() > 390:
            scoreA += 1
        else:
            scoreB += 1
        ball.goto(0, 0)
        ball.dx *= -1
        pen.clear()
        pen.write('Player A: {}  Player B: {}'.format(scoreA, scoreB), align='center', font=('Courier', 24, 'normal'))

    # Collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddleB.ycor() + 50 and ball.ycor() > paddleB.ycor() - 50:
        ball.setx(340)
        ball.dx *= -1
        os.system('aplay bounce.wav&')

    if (ball.xcor() < -340 and ball.xcor() > -350) and ball.ycor() < paddleA.ycor() + 50 and ball.ycor() > paddleA.ycor() - 60:
        ball.setx(-340)
        ball.dx *= -1
        os.system('aplay bounce.wav&')

    if scoreA == 11:
        endGame('A')
        furtherPlay = False
    if scoreB == 11:
        endGame('B')
        furtherPlay = False
