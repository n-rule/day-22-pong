from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, tuple_coordinates):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.coordinates = tuple_coordinates
        self.goto(self.coordinates)
        self.color('grey')
        self.refresh_scoreboard()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.refresh_scoreboard()

    def refresh_scoreboard(self):
        self.write(f'{self.score}', False, align='center', font=("Courier", 30, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f'GAME OVER BITCH', False, align='center', font=("Courier", 30, "bold"))
