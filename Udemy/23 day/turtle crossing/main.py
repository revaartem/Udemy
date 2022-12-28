import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

if __name__ == "__main__":

    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.bgpic('background.png')

    user_set_difficult = screen.textinput(title='Set game difficult', prompt=f'Choose starting car quantity.\n'
                                                                             f'Easy: < 10\n'
                                                                             f'Medium: 10 - 20\n'
                                                                             f'Hard: 20 - 40\n'
                                                                             f'Expert: > 40\n'
                                                                             f'Enter the desired quantity: ')

    player = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager(int(user_set_difficult))

    screen.listen()
    screen.onkeypress(player.move_down, 'Down')
    screen.onkeypress(player.move_up, 'Up')

    game_is_on = True
    while game_is_on:
        car_manager.all_cars_move(player.level)
        car_manager.car_home_position()
        if player.player_goto_next_level():
            scoreboard.next_level()
            car_manager.adding_cars(car_manager.cars_for_adding)
            car_manager.reset_car_position()
        if car_manager.car_collision(player):
            game_is_on = False
            scoreboard.game_over()
            continue

        time.sleep(0.1)
        screen.update()

    screen.exitonclick()
