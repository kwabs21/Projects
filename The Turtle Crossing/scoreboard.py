from turtle import Turtle

FONT = ("Courier", 16, "normal")
FONT_G_0 = ("Courier", 30, "bold")


class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.level = 1
            self.hideturtle()
            self.penup()
            self.goto(-290,265)
            self.update_scoreboard()


        def update_scoreboard(self):
            self.clear()
            self.write(f"Level: {self.level}", align="left", font=FONT)

        def increase_level(self):
            self.level += 1
            self.update_scoreboard()

        def game_over(self):
            self.goto(0,0)
            self.write("GAME OVER", align="center", font=FONT_G_0)
