from turtle import Turtle, Screen
from paddle import Paddle
from scoreBoard import ScoreBoard
from ball import Ball
from time import sleep

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MAX_SCORE = 1

screen = Screen()
screen.bgcolor("#3d84b8")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.tracer(0)

paddle_left = Paddle(((-1 * (SCREEN_WIDTH / 2)) + 20, 0), SCREEN_WIDTH,
                     SCREEN_HEIGHT)
paddle_right = Paddle((SCREEN_WIDTH / 2 - 20, 0), SCREEN_WIDTH, SCREEN_HEIGHT)

ball = Ball(SCREEN_WIDTH, SCREEN_HEIGHT)

score_board = ScoreBoard(SCREEN_WIDTH, SCREEN_HEIGHT)

screen.listen()
screen.onkey(key="Up", fun=paddle_right.move_up)
screen.onkey(key="Down", fun=paddle_right.move_down)

screen.onkey(key="w", fun=paddle_left.move_up)
screen.onkey(key="s", fun=paddle_left.move_down)

game_is_on = True
screen.update()

while game_is_on:
    sleep(0.05)
    ball.move()
    ball.bounce(paddle_right, paddle_left)
    score_update = ball.out_of_bounds_detect()
    if score_update[0] != 0:

        score_board.write_sent("Left paddle player won a point")
        sleep(1.5)
        score_board.lPoint()
        ball.reset()

    elif score_update[1] != 0:

        score_board.write_sent("Right paddle player won a point")
        sleep(1.5)
        score_board.rPoint()
        ball.reset()
        paddle_right.reset()
        paddle_left.reset()

    if score_board.r_score == MAX_SCORE or score_board.l_score == MAX_SCORE:
        score_board.game_over()
        game_is_on = False
    screen.update()

screen.exitonclick()
