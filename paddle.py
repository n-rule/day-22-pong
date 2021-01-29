from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, tuple_coordinates):
        super().__init__()
        self.shape('square')
        self.goto(tuple_coordinates)
        self.shapesize(5, 1)
        self.color('white', 'grey')
        self.penup()

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
