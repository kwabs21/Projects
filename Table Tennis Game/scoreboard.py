from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        # self.goto(-120, 200)
        # self.l_player = "Player 1"
        # self.write(self.l_player, align="center", font=("Courier", 50, "normal"))
        # self.goto(150, 200)
        # self.r_player = "Player 2"
        # self.write(self.r_player, align="center", font=("Courier", 50, "normal"))
        self.l_score = 0
        self.r_score = 0
        self.upate_scoreboard()


    def upate_scoreboard(self):
        self.clear()
        self.goto(-120, 170)
        self.l_player = "Player 1"
        self.write(self.l_player, align="center", font=("Courier", 30, "normal"))
        self.goto(120, 170)
        self.r_player = "Player 2"
        self.write(self.r_player, align="center", font=("Courier", 30, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.upate_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.upate_scoreboard()

    def game_over(self):
        self.penup()
        self.goto(0,10)
        self.end = "GAME OVER"
        self.write(self.end, align="center", font=("Courier", 50 , "bold"))