import time
from turtle import Screen


from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.tracer(0)

jim = Player()
cars = CarManager()
scoreboard = Scoreboard()


screen.listen()

screen.onkey(jim.go_up , "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()

    #Detection of collision with car
    for car in cars.all_cars:
        if car.distance(jim) < 20:
            game_is_on = False
            scoreboard.game_over()

    #Detect successful crossing
    if jim.at_finish_line():
        jim.go_to_start()
        cars.level_up()
        scoreboard.increase_level()

















screen.exitonclick()

