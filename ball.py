from turtle import Turtle
# from random import randint

initial_heading = 40


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")
        self.setheading(initial_heading)

    def move(self):
        self.fd(20)

    def bounce_side(self):
        self.setheading(360 - self.heading())

    def bounce_paddle_centre(self):
        self.setheading((360-self.heading()*2)/2)

    def bounce_paddle_side(self):
        self.setheading((360-self.heading()*2)/2 + 15)

    def reset_ball(self):
        self.goto(0, 0)
        self.setheading(initial_heading)

