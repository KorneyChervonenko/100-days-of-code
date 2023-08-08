""" paddle game """
import turtle
from paddle import BottomPaddle
from ball import Ball
from obstacles import Obstacle

def main():
    """ main function """
    screen = turtle.Screen()
    screen.setup()
    width = screen.window_width()
    height = screen.window_height()
    screen.screensize(width, height)
    screen.title('ball module')
    screen.bgcolor('green')
    screen.tracer(0)
    paddle = BottomPaddle()
    ball = Ball(paddle)
    screen.update()

    print(width, height, paddle.coord_y)
    screen.listen()

    game_is_over = False
    while not game_is_over:
        screen.ontimer(ball.move(), 5)

        if ball.touch(Obstacle.LEFT_WALL):
            # print('ball touched left wall')
            ball.d_x = -ball.d_x

        if ball.touch(Obstacle.RIGHT_WALL):
            # print('ball touched right wall')
            ball.d_x = -ball.d_x

        if ball.touch(Obstacle.UPPER_WALL):
            # print('ball touched upper wall')
            ball.d_y = -ball.d_y

        if ball.touch(Obstacle.BOTTOM_WALL):
            # print('ball touched bottom wall')
            ball.d_y = -ball.d_y
            game_is_over = True

        if (ball.ycor() <= paddle.coord_y + ball.size) and ball.touch(Obstacle.PADDLE):
            # print('ball touched paddle')
            # print(ball.ycor())
            ball.d_y = -ball.d_y

    screen.exitonclick()
    screen.mainloop()

if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
