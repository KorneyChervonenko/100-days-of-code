""" ball module """
import math
import random
import turtle
from obstacles import Obstacle
from paddle import BottomPaddle
INDENTATION = 20

# TODO
# сделать изменение направления через setheading
# проверять на столкновение с paddle только если шарик движется вниз и находится почти на дне
# проверять на столкновение со стенками только если шарик движется в том направлении. Стоит ли ?

class Ball(turtle.Turtle):
    """ ball class """
    ###
    STEP = 3
    def __init__(self, paddle: BottomPaddle = None) -> None:
        super().__init__()
        self.paddle = paddle
        self.shape('circle')
        self.size = self.shapesize()[0] * 20
        self.fillcolor('white')
        self.penup()
        self.speed("fastest")
        self.max_x = self.screen.window_width() // 2 - INDENTATION
        self.max_y = self.screen.window_height() // 2 - INDENTATION
        self.direction = random.choice((*range(225, 250), *range(290, 315)))
        self.d_x = int(self.STEP * math.cos(self.direction * math.pi / 180))
        self.d_y = int(self.STEP * math.sin(self.direction * math.pi / 180))
        # self.d_x = random.choice(range(1, self.STEP))
        # self.d_y = random.choice(range(1, self.STEP))


    def move(self):
        """ move ball one step"""
        x = self.xcor() + self.d_x
        y = self.ycor() + self.d_y
        self.goto(x, y)
        # self.forward(self.STEP)
        self.screen.update()

    def touch(self, obstacle: Obstacle):
        """ check if ball touch an obstacle """
        match obstacle:
            case Obstacle.LEFT_WALL:
                return self.xcor() <= -self.max_x
            case Obstacle.RIGHT_WALL:
                return self.xcor() >= self.max_x
            case Obstacle.UPPER_WALL:
                return self.ycor() >= self.max_y
            case Obstacle.BOTTOM_WALL:
                return self.ycor() <= -self.max_y
            case Obstacle.PADDLE:
                return bool(self.paddle) and any(self.distance(part) <= self.size for part in self.paddle.body)


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
    print(ball.size)
    # ball.setheading(90)
    screen.update()

    print(width, height, paddle.coord_y)
    screen.listen()
    # screen.onkey(screen.bye, 'Escape')

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

        if (ball.ycor() <= paddle.coord_y + ball.size) and ball.touch(Obstacle.PADDLE):
            # print('ball touched paddle')
            # print(ball.ycor())
            ball.d_y = -ball.d_y

        # screen.update()
        # ball.move()


    screen.exitonclick()
    screen.mainloop()


if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
