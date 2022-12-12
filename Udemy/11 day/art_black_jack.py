
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
#
# import random
# from art_black_jack import logo
#
#
# def cpu_card_decision(score):
#     if score < 10:
#         return True
#     elif score < 12:
#         decision = random.randint(1, 100)
#         if decision > 7:
#             return True
#         else:
#             return False
#     elif score < 14:
#         decision = random.randint(1, 100)
#         if decision > 30:
#             return True
#         else:
#             return False
#     elif score < 16:
#         decision = random.randint(1, 100)
#         if decision > 50:
#             return True
#         else:
#             return False
#     elif score < 18:
#         decision = random.randint(1, 100)
#         if decision > 70:
#             return True
#         else:
#             return False
#     elif score <= 20:
#         decision = random.randint(1, 100)
#         if decision > 98:
#             return True
#         else:
#             return False
#     elif score == 21:
#         return False
#
#
# def starting():
#     start_loop = True
#     while start_loop:
#         player_joice = input(f'\nDo you want to play Black Jack? Type "Yes" or "No"\n').lower()
#         if player_joice == 'no':
#             print('Good bye!')
#             start_loop -= 1
#             return False
#         elif player_joice == 'yes':
#             start_loop -= 1
#             return True
#         else:
#             print(f'''\n{'#' * 65}''')
#             print('     Your answer is out of my options. Please, try again.')
#             print(f'''{'#' * 65}\n''')
#
#
# def score_check(list_of_cards):
#     cards_def = list_of_cards
#     if sum(list_of_cards) == 22 and cards_def.count(11) == 2:
#         return True
#     elif sum(list_of_cards) > 21:
#         if 11 in cards_def:
#             cards_def.remove(11)
#             cards_def.append(1)
#             return list_of_cards == cards_def
#
#
# def game_process():
#     cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#     while starting():
#         print(logo)
#         my_cards = []
#         computer_cards = []
#         player_have_bj = False
#         cpu_have_bj = False
#         player_final_score = 0
#         player_final_hand = []
#         cpu_final_score = 0
#         cpu_final_hand = []
#
#         for _ in range(2):
#             my_cards.append(random.choice(cards))
#             computer_cards.append(random.choice(cards))
#
#         def player_play_turn(computer_hand, player_bj_statement, cpu_bj_statement,
#                              player_hand_final, player_score_final, player_cards):
#
#             current_score = sum(player_cards)
#
#             if current_score == 21:
#                 print('Player have Black Jack!')
#                 player_bj_statement += 1
#
#             elif sum(computer_hand) == 21:
#                 print('Computer have Black Jack!')
#                 cpu_bj_statement += 1
#
#             if score_check(player_cards):
#                 print('Player have Golden 22 with a pair of aces!')
#                 player_bj_statement += 1
#
#             if score_check(computer_hand):
#                 print('Computer have Golden 22 with a pair of aces!')
#                 cpu_bj_statement += 1
#
#             adding_cards = True
#             while adding_cards and not player_bj_statement and not cpu_bj_statement:
#                 current_score = sum(player_cards)
#                 score_check(player_cards)
#
#                 if current_score > 21:
#                     adding_cards -= 1
#                     continue
#
#                 elif current_score <= 21:
#
#                     print(f'''Your cards: {player_cards}, current score: {current_score}
#         Computer's first card: {max(computer_hand)}''')
#                     add_or_pass = input(f'''\nType "Y" to get another card, type "N" to pass: ''').lower()
#
#                     if add_or_pass != 'y' and add_or_pass != 'n':
#                         print(f'''\n{'#' * 45}''')
#                         print('   Wrong command. Please, type "Y" or "N"')
#                         print(f'''{'#' * 45}\n''')
#                         continue
#
#                     if add_or_pass == 'n':
#                         adding_cards -= 1
#                         continue
#
#                     if add_or_pass == 'y':
#                         player_cards.append(random.choice(cards))
#
#             else:
#                 player_hand_final += player_cards
#                 player_score_final += current_score
#                 print(f'\nYour final hand: {player_hand_final}, final score: {player_score_final}')
#                 if cpu_bj_statement or player_bj_statement:
#                     print(f'Computer final hand: {computer_hand}, final score: {sum(computer_hand)}')
#             return computer_hand == computer_hand, player_bj_statement == player_bj_statement, \
#                    cpu_bj_statement == cpu_bj_statement, player_hand_final == player_final_hand, \
#                    player_score_final == player_score_final, player_cards == player_cards
#
#         def cpu_play_turn():
#             nonlocal computer_cards, cpu_final_score, cpu_final_hand
#
#             adding_cards = True
#             while adding_cards:
#
#                 score_check(computer_cards)
#                 current_score = sum(computer_cards)
#
#                 if current_score > 21:
#                     # cpu_overload += 1
#                     cpu_final_hand += computer_cards
#                     cpu_final_score += current_score
#                     print(f'Computer final hand: {cpu_final_hand}, final score: {cpu_final_score}')
#                     adding_cards -= 1
#                     continue
#
#                 elif current_score <= 21:
#                     current_cpu_decision = cpu_card_decision(current_score)
#
#                     if current_cpu_decision:
#                         computer_cards.append(random.choice(cards))
#
#                     else:
#                         cpu_final_hand += computer_cards
#                         cpu_final_score += current_score
#                         adding_cards -= 1
#                         print(f'Computer final hand: {cpu_final_hand}, final score: {cpu_final_score}')
#                         continue
#
#         player_play_turn(computer_cards, player_have_bj, cpu_have_bj, player_final_hand, player_final_score, my_cards)
#
#         if not cpu_have_bj and not player_have_bj:
#             cpu_play_turn()
#
#             if cpu_final_score > 21 and player_final_score <= 21:
#                 print('Computer went over. Player win!')
#             elif player_final_score > 21 or player_final_score > 21 and cpu_final_score > 21:
#                 print('Player went over. Computer win!')
#             elif cpu_final_score < player_final_score <= 21:
#                 print('Player win!')
#             elif player_final_score < cpu_final_score <= 21:
#                 print('Computer win!')
#             elif player_final_score == cpu_final_score:
#                 print('Draw!')
#
#
# game_process()
