""" road module """
import turtle
import enum
import random
from pedestrian_module import Pedestrian
from road_module import Road


# STEP = 5
INDENTATION = 20
# RIGHT, LEFT, DOWN, UP = 0, 180, 270, 90

# class Direction(enum.Enum):
#     """ directions """
#     RIGHT = 0
#     LEFT = 180
#     DOWN = 270
#     UP = 90



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
    # pedestrian = Pedestrian((0, -max_y))
    # roads = [Road((max_x, 0), 5)]
    roads = {}
    roads[0] = Road((max_x, 0), 5)
    coord_y_set = set(range(0, max_y-INDENTATION, INDENTATION))
    coord_y_set |= set(range(0, INDENTATION-max_y, -INDENTATION))
    coord_y_set.discard(0)

    screen.listen()

    game_is_over = False
    pedestrian = None
    i = 0
    while not game_is_over:
        i += 1
        if not pedestrian and len(coord_y_set) == 0:
            print(sorted(road.start_y for road in roads.values()))
            lowest_road = min(list(roads.values()), key=lambda road: road.start_y)
            pedestrian = Pedestrian((0, lowest_road.start_y))
        elif pedestrian and (road_index:=int(pedestrian.ycor())) in roads:
            road = roads[road_index]
            # print(road_index, pedestrian.collide_with_any_car(road))
            if pedestrian.collide_with_any_car(road):
                # print(road_index)
                print('Game over')
                game_is_over = True
                break
        for road in roads.values():
            road.move_one_step()
        screen.update()
        screen.ontimer(None, 50)
        if len(coord_y_set) > 0:
            new_road_start_x = random.choice((max_x, -max_x))
            new_road_start_y = coord_y_set.pop()
            new_road_step = random.choice((2,3,4,5))
            new_road = Road((new_road_start_x, new_road_start_y), new_road_step)
            # roads.append(new_road)
            roads[new_road_start_y] = new_road
        elif i % 5 == 0:
            random_road = random.choice(list(roads.values()))
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
