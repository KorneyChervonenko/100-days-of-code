""" list of obstacles """
import enum
class Obstacle(enum.Enum):
    """ obstacles """
    RIGHT_WALL = enum.auto()
    LEFT_WALL = enum.auto()
    UPPER_WALL = enum.auto()
    BOTTOM_WALL = enum.auto()
    PADDLE = enum.auto()