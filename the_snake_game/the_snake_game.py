""" snake game """
import turtle
import random

class Snake(turtle.Turtle):
    """ snake class """
    STEP = 20
    RIGHT, LEFT, DOWN, UP = 0, 180, 270, 90

    def __init__(self, shape = "circle", color = 'white') -> None:
        super().__init__(shape)
        self.body = [self.position(), ]
        self.speed("fastest")
        self.original_color = color
        self.fillcolor(color)
        self.pencolor(color)
        self.penup()
        self.max_x = self.getscreen().window_width() // 2 - self.STEP
        self.max_y = self.getscreen().window_height() // 2 - self.STEP
        self.need_to_grow = False
        self.ready_to_turn = True

    def __len__(self):
        return len(self.body)

    def reset(self):
        """ reset color, stretch """
        self.fillcolor(self.original_color)
        self.shapesize(stretch_len=1, stretch_wid=1, outline=1)

    def in_canvas(self):
        """ check if snake is on canvas """
        return (-self.max_x <= self.xcor() <= self.max_x) and \
               (-self.max_y <= self.ycor() <= self.max_y)

    def can_bite(self, other: turtle.Turtle):
        """ check if head of snake can bite some another subject (turtle instance) """
        if self is other: # check if the snake can bite itself
            return any(int(self.distance(position)) == 0 for position in self.body[:-3])
        return int(self.distance(other)) == 0

    def eat(self, food: turtle.Turtle):
        """ snake eats food """
        self.fillcolor(food.fillcolor())
        self.shapesize(stretch_len=1.5, stretch_wid=1.5, outline=3)
        # self.screen.update()

    def move(self):
        """ move snake froward """
        self.stamp()
        if self.fillcolor() != self.original_color:
            self.reset()
        self.forward(self.STEP)

        self.body.append(self.position())
        if self.need_to_grow:
            self.need_to_grow = False
        else:
            self.clearstamps(1)
            self.body.pop(0)
        # self.screen.update()
        self.ready_to_turn = True

    def turn_right(self):
        """ turn snake right """
        if self.heading() != self.LEFT and self.ready_to_turn:
            self.setheading(self.RIGHT)
            self.ready_to_turn = False

    def turn_left(self):
        """ turn snake left """
        if self.heading() != self.RIGHT and self.ready_to_turn:
            self.setheading(self.LEFT)
            self.ready_to_turn = False

    def turn_down(self):
        """ turn snake down """
        if self.heading() != self.UP and self.ready_to_turn:
            self.setheading(self.DOWN)
            self.ready_to_turn = False

    def turn_up(self):
        """ turn snake right """
        if self.heading() != self.DOWN and self.ready_to_turn:
            self.setheading(self.UP)
            self.ready_to_turn = False

class Food(turtle.Turtle):
    """ piece of food """
    food_colors = ('red', 'yellow', 'magenta', 'dark violet', 'cyan', 'blue',)
    STEP = 20

    def __init__(self, shape = "circle") -> None:
        super().__init__(shape)
        self.penup()
        self.width = self.getscreen().window_width()
        self.height = self.getscreen().window_height()
        self.max_x = (int(self.width / 2 / self.STEP) - 2) * self.STEP
        self.max_y = (int(self.height / 2 / self.STEP) - 2) * self.STEP
        self.spawn()


    def spawn(self):
        """ change color and position """
        # select new color
        self.color(random.choice(self.food_colors))

        # select new position
        position_is_occupied = True
        while position_is_occupied:
            new_x = random.choice(range(-self.max_x, self.max_x, self.STEP))
            new_y = random.choice(range(-self.max_y, self.max_y, self.STEP))
            new_position = (new_x, new_y)
            position_is_occupied = False
            for subj in self.getscreen().turtles():
                if subj is self:
                    if self.distance(new_position) == 0:
                        position_is_occupied = True
                        break
                else:
                    if any(position == new_position for position in subj.body):
                        position_is_occupied = True
                        break
        self.setposition(new_position)
        # self.screen.update()

def main():
    """ main function """
    screen = turtle.Screen()
    screen.setup()
    width = screen.window_width()
    height = screen.window_height()
    screen.screensize(width, height)
    screen.title('snake')
    screen.bgcolor('green')
    screen.tracer(0)
    white_snake = Snake()
    somefood = Food()

    screen.listen()
    screen.onkey(white_snake.turn_up, 'Up')
    screen.onkey(white_snake.turn_down, 'Down')
    screen.onkey(white_snake.turn_left, 'Left')
    screen.onkey(white_snake.turn_right, 'Right')

    game_over = False
    while not game_over:
        screen.update()
        screen.ontimer(white_snake.move(), 200)

        if white_snake.can_bite(somefood):
            print('snake ate food')
            white_snake.eat(somefood)
            white_snake.need_to_grow = True
            somefood.spawn()

        if not white_snake.in_canvas():
            print('snake touched border')
            game_over = True

        if white_snake.can_bite(white_snake):
            print('snake bit itself')
            game_over = True

    screen.exitonclick()


def test():
    screen = turtle.Screen()
    screen.setup()
    width = screen.window_width()
    height = screen.window_height()
    screen.screensize(width, height)
    screen.title('snake')
    screen.bgcolor('green')
    screen.tracer(0)
    snake = Snake()
    screen.listen()
    for x in range(0, snake.max_x, 20):
        for y in range(0, snake.max_y, 20):
            new_position = (x, y)
            # print(new_position)
            snake.goto(new_position)
            snake.body.append(snake.position())
            snake.stamp()
            screen.update()
    food = Food()
    while True:
        food.spawn()
        food.stamp()

    screen.exitonclick()


if __name__ == "__main__":
    import sys
    import os
    os.system('cls')
    print('-----------------------------------------------------------')
    main()
    test()
    sys.exit()
