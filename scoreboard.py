from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.setpos(-20,270)
        self.penup()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.write(arg=f"Score : {self.score}", move=True, align="center", font=("courier", 20, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(-20,270)
        self.write(arg=f"Score : {self.score}", move=True, align="center", font=("courier", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER", move=True, align="center", font=("courier", 20, "normal"))
