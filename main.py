from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

left_position = [(-360, 40), (-360, 20), (-360, 0), (-360, -20), (-360, -40)]
right_position = [(360, 40), (360, 20), (360, 0), (360, -20), (360, -40)]

scoreboard_right_pos = (40, 270)
scoreboard_left_pos = (-40, 270)

screen = Screen()
lines = Turtle()
ball = Ball()
scoreboard_left = Scoreboard(scoreboard_left_pos)
scoreboard_right = Scoreboard(scoreboard_right_pos)
paddle_left = Paddle(left_position)
paddle_right = Paddle(right_position)


screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Welcome to my PONG")
screen.tracer(0)


lines.penup()
new_y = 0
for _ in range(25):
    lines.hideturtle()
    lines.goto(x=-2, y=-300+new_y)
    lines.pendown()
    lines.color("white")
    lines.fillcolor("white")
    lines.begin_fill()
    for side in range(2):
        lines.fd(4)
        lines.left(90)
        lines.fd(16)
        lines.left(90)
    lines.end_fill()
    lines.penup()
    new_y += 24


screen.listen()

screen.onkeypress(fun=paddle_left.move_up, key="w")
screen.onkeypress(fun=paddle_left.move_down, key="s")

screen.onkeypress(fun=paddle_right.move_up, key="Up")
screen.onkeypress(fun=paddle_right.move_down, key="Down")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    ball.move()

    if ball.ycor() >= 290 or ball.ycor() <= -290:
        ball.bounce_side()
        ball.move()

    elif ball.distance(paddle_right.segments[1]) < 25 or ball.distance(paddle_right.segments[2]) < 25 or \
            ball.distance(paddle_right.segments[3]) < 25 or ball.distance(paddle_left.segments[1]) < 25 or \
            ball.distance(paddle_left.segments[2]) < 25 or ball.distance(paddle_left.segments[3]) < 25:
        ball.bounce_paddle_centre()
        ball.move()

    elif ball.distance(paddle_right.segments[0]) < 25 or ball.distance(paddle_right.segments[4]) < 25 or \
            ball.distance(paddle_left.segments[0]) < 25 or ball.distance(paddle_left.segments[4]) < 25:
        ball.bounce_paddle_side()
        ball.move()

    elif ball.xcor() > 410:
        time.sleep(1)
        scoreboard_left.keep_score()
        ball.reset_ball()

    elif ball.xcor() < -410:
        time.sleep(1)
        scoreboard_right.keep_score()
        ball.reset_ball()

    elif scoreboard_left.score == 5:
        scoreboard_left.game_end()
        game_is_on = False

    elif scoreboard_right.score == 5:
        scoreboard_right.game_end()
        game_is_on = False

screen.exitonclick()
