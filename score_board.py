from turtle import Turtle, Screen

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.goto(0, 280)
        self.hideturtle()
        self.board()

    def board(self):
        self.write(f"Score = {self.score} ", move=False, align='center', font=('bold', 15, 'normal'))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.board()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over..",move=False, align ="center", font=("bold",15,"normal"))






