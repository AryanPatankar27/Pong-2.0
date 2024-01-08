import turtle
import time

wn = turtle.Screen()
wn.title("Pong by Aryan")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

point_a = 0
point_b = 0

paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("Player 1: 0   Player 2: 0", align="center", font=("Arial", 24, "normal"))

difficulty_text = turtle.Turtle()
difficulty_text.speed(0)
difficulty_text.color("white")
difficulty_text.penup()
difficulty_text.hideturtle()
difficulty_text.goto(0, 220)
difficulty_text.write("Choose Difficulty: Easy (E), Medium (M), Difficult (D)", align="center", font=("Arial", 16, "normal"))

level = "easy"

def set_difficulty(difficulty):
    global level
    level = difficulty
    difficulty_text.clear()
    difficulty_text.write("Difficulty: {}".format(difficulty.capitalize()), align="center", font=("Arial", 16, "normal"))

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(lambda: set_difficulty("easy"), "e")
wn.onkeypress(lambda: set_difficulty("medium"), "m")
wn.onkeypress(lambda: set_difficulty("difficult"), "d")

while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        point_a += 1
        score.clear()
        score.write("Player 1: {}   Player 2: {} ".format(point_a, point_b), align="center", font=("Arial", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        point_b += 1
        score.clear()
        score.write("Player 1: {}   Player 2: {} ".format(point_a, point_b), align="center", font=("Arial", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    if level == "easy":
        ball_speed = 0.25
    elif level == "medium":
        ball_speed = 0.5
    elif level == "difficult":
        ball_speed = 0.75

    time.sleep(0.01)
