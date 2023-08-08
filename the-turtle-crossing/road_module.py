""" road module """
import turtle
import enum
import random
from car_module import Car
from directions_module import Direction

# STEP = 5
INDENTATION = 20
# RIGHT, LEFT, DOWN, UP = 0, 180, 270, 90

# class Direction(enum.Enum):
#     """ directions """
#     RIGHT = 0
#     LEFT = 180
#     DOWN = 270
#     UP = 90

class Road:
    """ road class """
    # STEP = 5
    def __init__(self, start_position, step) -> None:
        self.start_position = start_position
        self.start_x, self.start_y = start_position
        self.direction = Direction.RIGHT if self.start_x < 0 else Direction.LEFT
        self.step = step
        self.max_number_of_cars = 5
        self.cars = [Car(self.start_position, self.direction, self.step), ]
        self.screen = self.cars[0].screen
        # self.screen.update()

    def add_car(self):
        """ add new car on the road """
        ### distance from previous car must be greater than INDENTATION
        if len(self.cars) < self.max_number_of_cars:
            new_car = Car(self.start_position, self.direction, self.step)
            if len(self.cars) == 0:
                self.cars.append(new_car)
            else:
                last_car = self.cars[-1]
                if last_car.distance(new_car) > 2 * INDENTATION:
                    self.cars.append(new_car)
                else:
                    new_car.hideturtle()
                    del new_car
        return self

    def move_one_step(self):
        """ move all cars 1 step """
        for car in self.cars:
            car.move_one_step()
        if len(self.cars) > 0:
            if not self.cars[0].is_on_canvas():
                first_car = self.cars.pop(0)
                first_car.hideturtle()
                del first_car
                self.add_car()



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
    max_x = screen.window_width() // 2 - INDENTATION
    max_y = screen.window_height() // 2 - INDENTATION
    print(width, height, max_x, max_y)

    roads = [Road((max_x, 0), 5)]
    coord_y_set = set(range(0, max_y-INDENTATION, INDENTATION))
    coord_y_set |= set(range(0, INDENTATION-max_y, -INDENTATION))
    coord_y_set.discard(0)

    screen.listen()

    game_is_over = False
    i = 0
    while not game_is_over:
        i += 1
        # road.move_one_step(STEP)
        # road2.move_one_step(STEP)
        for road in roads:
            road.move_one_step()
        screen.update()
        screen.ontimer(None, 50)
        if len(coord_y_set) > 0:
            new_road_start_x = random.choice((max_x, -max_x))
            new_road_step = random.choice((2,3,4,5))
            new_road = Road((new_road_start_x, coord_y_set.pop()),new_road_step)
            roads.append(new_road)
        elif i % 5 == 0:
            random_road = random.choice(roads)
            random_road.add_car()

    #     pass
    screen.exitonclick()
    screen.mainloop()

if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    sys.exit()
