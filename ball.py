from turtle import Turtle
import random

DIRECTION = [1, -1]


class Ball(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.screen_height = screen_height / 2
        self.screen_width = screen_width / 2
        self.x_move = 10 * (random.choice(DIRECTION))
        self.y_move = 10 * (random.choice(DIRECTION))
        self.speed = 0

    def move(self):
        # moving by 10 pixels each time
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self, right_paddle, left_paddle):
        # the boundary case
        if self.ycor() >= self.screen_height - 10 or self.ycor() <= (
                -1 * self.screen_height) + 10:
            self.y_move *= -1
        # right paddle case
        elif self.distance(right_paddle.position()) < 50 and \
                right_paddle.xcor() - self.xcor() <= 20:
            self.speed += 2
            self.x_move = -10 - self.speed
            # self.y_move *= -1

        elif self.distance(left_paddle.position()) < 50 and \
                self.xcor() - left_paddle.xcor() <= 20:
            self.speed += 2
            self.x_move = 10 + self.speed
            # self.y_move *= -1

    def out_of_bounds_detect(self):
        if self.xcor() >= self.screen_width - 10:
            return 1, 0
        elif self.xcor() <= (-1 * self.screen_width) - 10:
            return 0, 1
        return 0, 0

    def reset(self):
        self.goto(0, 0)
        self.speed = 0
        self.x_move = 10 * (random.choice(DIRECTION))
        self.y_move = 10 * (random.choice(DIRECTION))
