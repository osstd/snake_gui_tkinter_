from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.type_()

    def type_(self):
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"The score is: {self.score} High score: {self.high_score}", False, "center",
                   ("Arial", 24, "normal"))

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def hit_your_tail(self):
        self.goto(0, -30)
        self.write("You have hit your tail", False, "center", ("Arial", 30, "normal"))
