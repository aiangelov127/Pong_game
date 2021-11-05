from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(position)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def game_end(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def keep_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()