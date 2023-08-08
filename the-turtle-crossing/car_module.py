""" car module """
import turtle
import random
import enum

# STEP = 1
INDENTATION = 20
# RIGHT, LEFT, DOWN, UP = 0, 180, 270, 90

class Direction(enum.Enum):
    """ directions """
    RIGHT = 0
    LEFT = 180
    DOWN = 270
    UP = 90


class Car(turtle.Turtle):
    """ Car class """
    def __init__(self, position: tuple, direction: Direction, step: int = 5) -> None:
        super().__init__()
        self.step = step
        self.speed('fastest')
        self.shape('square')
        # self.shapesize(stretch_len=random.choice(range(1,4)))
        self.fillcolor(random.choice(('red', 'yellow', 'magenta', 'dark violet', 'cyan', 'blue',)))
        self.setheading(direction.value)
        # self.setposition(position)
        self.penup()
        self.setposition(position)
        self.max_x = self.screen.window_width() // 2 - INDENTATION
        self.screen.update()

    def is_on_canvas(self) -> bool:
        """ check if car is on canvas """
        return (self.heading() == Direction.RIGHT.value and self.xcor() < self.max_x) or \
               (self.heading() == Direction.LEFT.value and self.xcor() > -self.max_x)

    def move_one_step(self):
        """ move car 1 step """
        self.forward(self.step)
        # self.screen.update()



def main():
    """ main function """
    screen = turtle.Screen()
    screen.setup()
    width = screen.window_width()
    height = screen.window_height()
    screen.screensize(width, height)
    screen.title('Car module')
    screen.bgcolor('green')
    screen.tracer(0)
    max_x = screen.window_width() // 2 - INDENTATION
    # max_y = screen.window_height() // 2 - INDENTATION
    car = Car((max_x,0), Direction.LEFT)
    car2 = Car((-max_x,20), Direction.RIGHT)
    screen.update()
    screen.listen()

    # game_is_over = False
    while car.is_on_canvas():
    # while not game_is_over:
        screen.ontimer(car.move_one_step(), 5)
        screen.ontimer(car2.move_one_step(), 5)
        screen.update()
        # car.move_one_step(STEP)
    screen.exitonclick()
    screen.mainloop()

if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
