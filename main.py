import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

scoreboard = Scoreboard()
car_manager = CarManager()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player((0, -280))

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.generate()
    car_manager.move_cars()
    for _ in car_manager.all_cars:
        if player.distance(_) < 20:
            game_is_on = False
            scoreboard.game_over()
    if player.ycor() > 250:
        player.goto(0, -280)
        car_manager.accelerate_cars()
        scoreboard.mark_level()




screen.exitonclick()
