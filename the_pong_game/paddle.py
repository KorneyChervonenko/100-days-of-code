""" paddle """
import turtle
# import random
STEP = 20
INDENTATION = 20
RIGHT, LEFT, DOWN, UP = 0, 180, 270, 90

class PaddlePart(turtle.Turtle):
    """ paddle class """
    def __init__(self, x=0, y=0) -> None:
        super().__init__()
        self.shape('square')
        self.fillcolor('white')
        self.penup()
        self.speed("fastest")
        self.setposition(x, y)

    def __repr__(self) -> str:
        return f'{self.position()}'

class BottomPaddle:
    """ bottom paddle class """
    def __init__(self, size=2) -> None:
        self.screen = turtle.Screen()
        self.max_x = self.screen.window_width() // 2 - INDENTATION
        self.coord_y = -self.screen.window_height() // 2 + 2 * INDENTATION

        self.body = [PaddlePart(0, self.coord_y),]
        for _ in range(size):
            self.increase()

        self.screen.onkeypress(self.step_left, 'Left')
        self.screen.onkeypress(self.step_right, 'Right')
        self.screen.onkey(self.increase, 'plus')
        self.screen.onkey(self.decrease, 'minus')

    @property
    def center_part(self):
        """ return center of the paddle """
        return self.body[len(self.body) // 2]

    def step_right(self):
        """ move paddle right 1 STEP """
        if self.center_part.xcor() + STEP < self.max_x:
            right_part = self.body[-1]
            left_part = self.body.pop(0)
            left_coord_x = right_part.xcor() + STEP
            left_part.setposition(left_coord_x, self.coord_y)
            self.body.append(left_part)
            self.screen.update()

    def step_left(self):
        """ move paddle left 1 STEP """
        if self.center_part.xcor() - STEP > -self.max_x:
            left_part = self.body[0]
            right_part = self.body.pop()
            right_coord_x = left_part.xcor() - STEP
            right_part.setposition(right_coord_x, self.coord_y)
            self.body.insert(0, right_part)
            self.screen.update()

    def increase(self):
        """ increase paddle length """
        left_part = self.body[0]
        right_part = self.body[-1]
        new_left_part = PaddlePart(left_part.xcor()-STEP, self.coord_y)
        new_right_part = PaddlePart(right_part.xcor()+STEP, self.coord_y)
        self.body.append(new_right_part)
        self.body.insert(0, new_left_part)
        self.screen.update()
        return self

    def decrease(self):
        """ decrease paddle length """
        if len(self.body) > 1:
            left_part = self.body[0]
            right_part = self.body[-1]
            self.body = self.body[1:-1]
            left_part.hideturtle()
            del left_part
            right_part.hideturtle()
            del right_part
            self.screen.update()
        return self


def main():
    """ main function """
    screen = turtle.Screen()
    screen.setup()
    width = screen.window_width()
    height = screen.window_height()
    screen.screensize(width, height)
    screen.title('paddle module')
    screen.bgcolor('green')
    screen.tracer(0)
    # paddle = PaddlePart()
    bottom_paddle = BottomPaddle()
    screen.update()
    screen.listen()

    # while True:
    #     # screen.ontimer(screen.update(), 1)
    #     # screen.update()
    #     pass


    screen.exitonclick()
    print(bottom_paddle.body)
    print(bottom_paddle.center_part)

if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()


    # def step_right(self):
    #     """ move paddle right 1 STEP """
    #     for part in self.body:
    #         part.setheading(RIGHT)
    #         part.forward(STEP)
    #     self.screen.update()

    # def step_left(self):
    #     """ move paddle left 1 STEP """
    #     for part in self.body:
    #         part.setheading(LEFT)
    #         part.forward(STEP)
    #     self.screen.update()


    # def step_right(self):
    #     """ move paddle right 1 STEP """
    #     for part in self.body:
    #         new_x = part.xcor() + STEP
    #         part.goto(new_x, self.coord_y)
    #     self.screen.update()

    # def step_left(self):
    #     """ move paddle left 1 STEP """
    #     for part in self.body:
    #         new_x = part.xcor() - STEP
    #         part.goto(new_x, self.coord_y)
    #     self.screen.update()