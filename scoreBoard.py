from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.color("#f5f7b2")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.screen_height = screen_height / 2
        self.screen_width = screen_width / 2
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, self.screen_height - 50)
        self.write(arg=self.l_score, align="left",
                   font=("Courier", 36, "normal"))
        self.goto(100, self.screen_height - 50)
        self.write(arg=self.r_score, align="right",
                   font=("Courier", 36, "normal"))

    def lPoint(self):
        self.l_score += 1
        self.update()

    def rPoint(self):
        self.r_score += 1
        self.update()

    def game_over(self):
        self.clear()
        self.color("#f8a488")
        self.goto(0, self.screen_height / 2)
        if self.l_score > self.r_score:
            self.write(arg="GAME OVER", align="center",
                       font=("Courier", 50, "normal"))
            self.goto(0, (-1 * self.screen_height) / 2)
            self.write(arg="LEFT PLAYER WINS", align="center",
                       font=("Courier", 50, "normal"))

        else:
            self.write(arg="GAME OVER", align="center",
                       font=("Courier", 50, "normal"))
            self.goto(0, (-1 * self.screen_height / 2))
            self.write(arg="RIGHT PLAYER WINS", align="center",
                       font=("Courier", 50, "normal"))

    def write_sent(self, sentence):
        self.goto(0, 0)
        self.write(arg=sentence, align="center",
                   font=("Courier", 36, "normal"))
