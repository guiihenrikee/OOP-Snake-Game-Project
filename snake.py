from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def move(self):
        for snake_piece in range(len(self.snakes) - 1, 0, -1):
            new_x = self.snakes[snake_piece - 1].xcor()
            new_y = self.snakes[snake_piece - 1].ycor()
            self.snakes[snake_piece].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def create_snake(self):
        for turtle in STARTING_POSITIONS:
            self.add_segment(turtle)

    def add_segment(self, turtle):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("orange")
        snake.shapesize(0.9, 0.9)
        snake.goto(turtle)
        self.snakes.append(snake)

    def head_mod(self):
        self.head.color("cyan")
        self.head.shape("circle")
        self.head.shapesize(0.8, 0.9)

    def extend(self):  # Extend the snake
        self.add_segment(self.snakes[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            
    def reset(self):
        for seg in self.snakes:
            seg.goto(1000, 1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]
