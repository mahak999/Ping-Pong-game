from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position,  screen_width, screen_height):
        super().__init__()
        self.shape("square")
        self.color("#233e8b")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.initial_position = position
        self.goto(self.initial_position)
        self.screen_width = screen_width/2
        self.screen_height = screen_height/2

    def move_up(self):
        new_y = self.ycor() + 30
        if new_y < self.screen_height:
            self.sety(new_y)

    def move_down(self):
        new_y = self.ycor() - 30
        if new_y > (-1 * self.screen_height):
            self.sety(new_y)

    def reset(self):
        self.goto(self.initial_position)
