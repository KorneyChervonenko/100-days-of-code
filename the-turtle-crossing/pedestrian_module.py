""" road module """
import turtle
import enum
import functools
from directions_module import Direction

# STEP = 20
INDENTATION = 20
# RIGHT, LEFT, DOWN, UP = 0, 180, 270, 90

# class Direction(enum.Enum):
#     """ directions """
#     RIGHT = 0
#     LEFT = 180
#     DOWN = 270
#     UP = 90

class Pedestrian(turtle.Turtle):
    """ Pedestrian class """
    def __init__(self, position: tuple = (0, 0)) -> None:
        super().__init__()
        self.step = 20
        self.shape('turtle')
        self.speed("fastest")
        self.fillcolor('black')
        self.penup()
        self.max_x = self.screen.window_width() // 2 - INDENTATION
        self.max_y = self.screen.window_height() // 2 - INDENTATION
        self.setheading(Direction.UP.value)
        self.setposition(position)
        self.screen.onkeypress(self.move_up, 'Up')
        self.screen.onkeypress(self.move_down, 'Down')
        self.screen.onkeypress(self.move_left, 'Left')
        self.screen.onkeypress(self.move_right, 'Right')
        self.screen.update()

    def in_canvas(self):
        """ check if pedestrian is on canvas """
        return (-self.max_x <= self.xcor() <= self.max_x) and \
               (-self.max_y <= self.ycor() <= self.max_y)

    def collide_with_any_car(self, road) -> bool:
        """ check if head of pedestrian can bite some another subject (turtle instance) """
        return any(self.distance(car) < self.step for car in road.cars)

    def move_one_step(self, direction: Direction = None):
        """ move pedestrian forward 1 STEP to selected direction"""
        self.setheading(direction.value)
        self.forward(self.step)
        if not self.in_canvas():
            # print('pedestrian is out of sight')
            self.backward(self.step)
        self.screen.update()

    move_up = functools.partialmethod(move_one_step, direction = Direction.UP)
    move_down = functools.partialmethod(move_one_step, direction = Direction.DOWN)
    move_left = functools.partialmethod(move_one_step, direction = Direction.LEFT)
    move_right = functools.partialmethod(move_one_step, direction = Direction.RIGHT)

    # def move_up(self):
    #     return self.move(direction = Direction.UP)
    # def move_down(self):
    #     return self.move(direction = Direction.DOWN)
    # def move_left(self):
    #     return self.move(direction = Direction.LEFT)
    # def move_right(self):
    #     return self.move(direction = Direction.RIGHT)



def main():
    """ main function """
    screen = turtle.Screen()
    screen.setup(width=0.5, height=0.5)
    width = screen.window_width()
    height = screen.window_height()
    screen.screensize(width, height)
    screen.title('Road module')
    screen.bgcolor('green')
    screen.tracer(0)
    # print(width, height, max_x, max_y)
    pedestrian = Pedestrian()



    screen.listen()
    screen.exitonclick()
    screen.mainloop()

if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
