import time
from turtle import Screen

from ball import *
from paddle import *
from scoreboard import *

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.title('PONG - Ultimate Edition')
screen.bgcolor('black')

r_score = 0
l_score = 0

r_scoreboard = Scoreboard((50, 240))
l_scoreboard = Scoreboard((-50, 240))
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

while True:
    ball.move()
    time.sleep(ball.move_speed)
    screen.update()

    # Wall Collision
    if ball.ycor() >= 275 or ball.ycor() <= -275:
        ball.wall_bounce()

    #     Paddle Collision

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330 or ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()

    if ball.xcor() > 380:
        l_scoreboard.increase_score()
        ball.reset()
        ball.paddle_bounce()

    if ball.xcor() < -380:
        r_scoreboard.increase_score()
        ball.reset()
        ball.paddle_bounce()

screen.exitonclick()
