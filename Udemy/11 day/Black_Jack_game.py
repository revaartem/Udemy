from func_for_bj import starting, card_generator, player_play_turn, cpu_play_turn, final_result
from art_black_jack import logo


def game_process():
    """The main function of programme, including all the functions of the game.
    In this function you can edit list of cards and see, how work logic of the programme."""

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

        my_cards, computer_cards = card_generator(my_cards, computer_cards, cards)

        computer_cards, player_have_bj, cpu_have_bj, player_final_hand, player_final_score, my_cards = \
            player_play_turn \
                (computer_cards, player_have_bj, cpu_have_bj, player_final_hand, player_final_score, my_cards, cards)

        if not cpu_have_bj and not player_have_bj:
            computer_cards, cpu_final_score, cpu_final_hand, cards = cpu_play_turn \
                (computer_cards, cpu_final_score, cpu_final_hand, cards)

        final_result(cpu_final_score, player_final_score, player_have_bj, cpu_have_bj)


game_process()