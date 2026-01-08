import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score1 = 0
score2 = 0

# Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid=5, stretch_len=1)
paddle1.penup()
paddle1.goto(-350, 0)

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.shape("square")
paddle2.color("white")
paddle2.shapesize(stretch_wid=5, stretch_len=1)
paddle2.penup()
paddle2.goto(350, 0)

# Ball
START_SPEED = 0.1
SPEED_INCREMENT = 0.005

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)
ball.dx = START_SPEED
ball.dy = START_SPEED

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0   Player 2: 0", align="center", font=("Courier", 24, "normal"))


# Functions For Paddle Movements
def paddle1_up():
    y = paddle1.ycor()
    y += 20
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y -= 20
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y += 20
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y -= 20
    paddle2.sety(y)

# Keyboard Bindings
wn.listen()
wn.onkeypress(paddle1_up, "w")
wn.onkeypress(paddle1_down, "s")
wn.onkeypress(paddle2_up, "Up")
wn.onkeypress(paddle2_down, "Down")

# Main Game Loop
while True:
    wn.update()

    # Ball Movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border Checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = -START_SPEED
        ball.dy = START_SPEED
        score1 += 1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = START_SPEED
        ball.dy = START_SPEED
        score2 += 1
        pen.clear()
        pen.write("Player 1: {}   Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    # Paddle - Ball Collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle2.ycor() + 40 and ball.ycor() > paddle2.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

        ball.dx += SPEED_INCREMENT if ball.dx > 0 else -SPEED_INCREMENT
        ball.dy += SPEED_INCREMENT if ball.dy > 0 else -SPEED_INCREMENT

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle1.ycor() + 40 and ball.ycor() > paddle1.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1

        ball.dx += SPEED_INCREMENT if ball.dx > 0 else -SPEED_INCREMENT
        ball.dy += SPEED_INCREMENT if ball.dy > 0 else -SPEED_INCREMENT