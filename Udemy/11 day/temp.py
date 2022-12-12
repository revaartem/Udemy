
import random
from art_black_jack import logo


def cpu_card_decision(score):
    if score < 10:
        return True
    elif score < 12:
        decision = random.randint(1, 100)
        if decision > 7:
            return True
        else:
            return False
    elif score < 14:
        decision = random.randint(1, 100)
        if decision > 30:
            return True
        else:
            return False
    elif score < 16:
        decision = random.randint(1, 100)
        if decision > 50:
            return True
        else:
            return False
    elif score < 18:
        decision = random.randint(1, 100)
        if decision > 70:
            return True
        else:
            return False
    elif score <= 20:
        decision = random.randint(1, 100)
        if decision > 98:
            return True
        else:
            return False
    elif score == 21:
        return False


def starting():
    start_loop = True
    while start_loop:
        player_joice = input(f'\nDo you want to play Black Jack? Type "Yes" or "No"\n').lower()
        if player_joice == 'no':
            print('Good bye!')
            start_loop -= 1
            return False
        elif player_joice == 'yes':
            start_loop -= 1
            return True
        else:
            print(f'''\n{'#' * 65}''')
            print('     Your answer is out of my options. Please, try again.')
            print(f'''{'#' * 65}\n''')


def score_check(list_of_cards):
    cards_def = list_of_cards
    if sum(list_of_cards) == 22 and cards_def.count(11) == 2:
        return True
    elif sum(list_of_cards) > 21:
        if 11 in cards_def:
            cards_def.remove(11)
            cards_def.append(1)
            return list_of_cards == cards_def


def game_process():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    while starting():
        print(logo)
        my_cards = []
        computer_cards = []
        player_have_bj = False
        cpu_have_bj = False
        player_final_score = 0
        player_final_hand = []
        cpu_final_score = 0
        cpu_final_hand = []

        for _ in range(2):
            my_cards.append(random.choice(cards))
            computer_cards.append(random.choice(cards))

        def player_play_turn():

            nonlocal computer_cards, player_have_bj, cpu_have_bj, player_final_hand, player_final_score

            current_score = sum(my_cards)

            if current_score == 21:
                print('Player have Black Jack!')
                player_have_bj += 1

            elif sum(computer_cards) == 21:
                print('Computer have Black Jack!')
                cpu_have_bj += 1

            if score_check(my_cards):
                print('Player have Golden 22 with a pair of aces!')
                player_have_bj += 1

            if score_check(computer_cards):
                print('Computer have Golden 22 with a pair of aces!')
                cpu_have_bj += 1

            adding_cards = True
            while adding_cards and not player_have_bj and not cpu_have_bj:
                current_score = sum(my_cards)
                score_check(my_cards)

                if current_score > 21:
                    adding_cards -= 1
                    continue

                elif current_score <= 21:

                    print(f'''Your cards: {my_cards}, current score: {current_score}
        Computer's first card: {max(computer_cards)}''')
                    add_or_pass = input(f'''\nType "Y" to get another card, type "N" to pass: ''').lower()

                    if add_or_pass != 'y' and add_or_pass != 'n':
                        print(f'''\n{'#' * 45}''')
                        print('   Wrong command. Please, type "Y" or "N"')
                        print(f'''{'#' * 45}\n''')
                        continue

                    if add_or_pass == 'n':
                        adding_cards -= 1
                        continue

                    if add_or_pass == 'y':
                        my_cards.append(random.choice(cards))

            else:
                player_final_hand += my_cards
                player_final_score += current_score
                print(f'\nYour final hand: {player_final_hand}, final score: {player_final_score}')
                if cpu_have_bj or player_have_bj:
                    print(f'Computer final hand: {computer_cards}, final score: {sum(computer_cards)}')

        def cpu_play_turn():
            nonlocal computer_cards, cpu_final_score, cpu_final_hand

            adding_cards = True
            while adding_cards:

                score_check(computer_cards)
                current_score = sum(computer_cards)

                if current_score > 21:
                    # cpu_overload += 1
                    cpu_final_hand += computer_cards
                    cpu_final_score += current_score
                    print(f'Computer final hand: {cpu_final_hand}, final score: {cpu_final_score}')
                    adding_cards -= 1
                    continue

                elif current_score <= 21:
                    current_cpu_decision = cpu_card_decision(current_score)

                    if current_cpu_decision:
                        computer_cards.append(random.choice(cards))

                    else:
                        cpu_final_hand += computer_cards
                        cpu_final_score += current_score
                        adding_cards -= 1
                        print(f'Computer final hand: {cpu_final_hand}, final score: {cpu_final_score}')
                        continue

        player_play_turn()

        if not cpu_have_bj and not player_have_bj:
            cpu_play_turn()

        if cpu_final_score > 21 and player_final_score <= 21:
            print('Computer went over. Player win!')
        elif player_final_score > 21 or player_final_score > 21 and cpu_final_score > 21:
            print('Player went over. Computer win!')
        elif cpu_final_score < player_final_score and player_final_score <= 21:
            print('Player win!')
        elif player_final_score < cpu_final_score and cpu_final_score <= 21:
            print('Computer win!')
        elif player_final_score == cpu_final_score:
            print('Draw!')


game_process()
