from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from  scoreboard import Scoreboard


screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))

ball = Ball()

score_board = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor()>= 290 or ball.ycor() <=-290:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320  or  ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score_board.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score_board.r_point()

    if score_board.l_score == 10 or score_board.r_score == 10:
        game_is_on = False
        score_board.game_over()



screen.exitonclick()