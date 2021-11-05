from turtle import Turtle

PADDLE_SPEED = 20


class Paddle:

    def __init__(self, starting_position):
        self.starting_position = starting_position
        self.segments = []
        self.paddle_position()
        self.paddle_top = self.segments[0]
        self.paddle_bottom = self.segments[4]

    def paddle_position(self):
        for position in self.starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        paddle = Turtle("square")
        paddle.penup()
        paddle.color("white", "white")
        paddle.goto(position)
        self.segments.append(paddle)

    def move_up(self):
        for paddle_num in range((len(self.segments)-1), 0, -1):
            new_y = self.segments[paddle_num-1].ycor()
            new_x = self.segments[paddle_num].xcor()
            self.segments[paddle_num].goto(x=new_x, y=new_y)
        self.paddle_top.setheading(90)
        self.paddle_top.fd(PADDLE_SPEED)

    def move_down(self):
        for paddle_num in range(len(self.segments)-1):
            new_y = self.segments[paddle_num+1].ycor()
            new_x = self.segments[paddle_num].xcor()
            self.segments[paddle_num].goto(x=new_x, y=new_y)
        self.paddle_bottom.setheading(270)
        self.paddle_bottom.fd(PADDLE_SPEED)
