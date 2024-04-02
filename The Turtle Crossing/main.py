import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from player import Player

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create objects
player = Player()
car_manager = CarManager()
scorebboard = Scoreboard()


# Listen for key events
screen.listen()
screen.onkey(player.go_up, "Up")


# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    #Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 23:
            game_is_on = False
            scorebboard.game_over()

    #Detect successful crossinh
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scorebboard.increase_level()

screen.exitonclick()

