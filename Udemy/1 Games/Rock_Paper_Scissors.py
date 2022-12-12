from art_for_rock_paper_scissors import logo
import random
"""In this game, the user can play a classic game with the CPU. 
The player can choose the number of rounds. After all rounds are completed, 
the final score and the name of the winner are displayed."""


def greeting():
    """This function will greet the player and tell him the rules of the game."""

    print(logo)
    print('''Hello dear player!
This is "Rock Paper Scissors" game, where your opponent will be the CPU.
The rules of the game are standard:
Rock beats Scissors
Scissors beats Paper
Paper beat Rock

You can set the number of rounds.

Good luck!''')


def round_number():
    """In this function player enters the number of rounds.
    The function implements protection against incorrect user input."""

    number_of_rounds = input('Please set the number of rounds: ')
    try:
        number_of_rounds = int(number_of_rounds)
    except TypeError and ValueError:
        print('Error.'
              '\nOnly digits in this field.Try again.'
              '\n')
    if type(number_of_rounds) != int:
        while number_of_rounds != int:
            number_of_rounds = input('Please set the number of rounds: ')
            try:
                int(number_of_rounds)
            except TypeError and ValueError:
                print('Error.'
                      '\nOnly digits in this field.Try again.'
                      '\n')
            else:
                break
    return int(number_of_rounds)


def game_engine():
    """This is the main function that is responsible for the course of the game.
    Here the user enters commands."""

    greeting()
    print("\nLets started!\n")

    number_of_rounds = int(round_number())
    cpu_wins = 0
    player_wins = 0
    for _ in range(number_of_rounds):
        player_turn = input('Enter your choice from rock, paper or scissors: ')
        player_turn = player_turn.lower()
        operator_base = ['rock', 'paper', 'scissors']
        if player_turn not in operator_base:
            while player_turn not in operator_base:
                print('\nWrong operator.'
                      '\nPlease use only rock, paper or scissors.'
                      '\n')
                player_turn = input('Enter your choice from rock, paper or scissors: ')
        cpu_turn = operator_base[random.randint(0, 2)]
        beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
        if beats[player_turn] == cpu_turn:
            print(f'Player - {player_turn}'
                  f'\nCPU - {cpu_turn}'
                  f'\n')
            print("Player win this round!")
            player_wins += 1
        if beats[cpu_turn] == player_turn:
            print(f'Player - {player_turn}'
                  f'\nCPU - {cpu_turn}'
                  f'\n')
            print("CPU win this round!")
            cpu_wins += 1
        if player_turn == cpu_turn:
            print("Draw!")
    print(f'\nOk, all rounds left, time to know who is the winner...'
          f'\nPlayer - {player_wins} win'
          f'\nCPU - {cpu_wins} win'
          f'\n')
    if player_wins > cpu_wins:
        print('Player win the game!!!')
    elif cpu_wins > player_wins:
        print('CPU win the game!!!')
    else:
        print('Total draw!!!')


game_engine()
