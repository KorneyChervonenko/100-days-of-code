""" list of Directions """
import enum
class Direction(enum.Enum):
    """ obstacles """
    RIGHT = 0
    LEFT = 180
    DOWN = 270
    UP = 90


print(Direction.LEFT.value)