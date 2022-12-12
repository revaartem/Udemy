from art_blind_game import logo

print(logo)

names_and_bids = {}


def game_engine():
    player_adding = True
    while player_adding:
        name_input = input('What is your name?: ')
        bid_input = int(input('What is your bid?: $'))
        names_and_bids[name_input] = bid_input
        other_players = input('Are there any other players?\nType "Yes" or "No": ').lower()
        if other_players == 'no':
            player_adding -= 1
        print('\n' * 60)


name_of_winner = ''
winner_bid = 0


def bid_matching():
    global name_of_winner
    global winner_bid
    list_of_bids = []
    for value in names_and_bids.values():
        list_of_bids.append(value)
    for key, value in names_and_bids.items():
        if value == max(list_of_bids):
            name_of_winner += key
            winner_bid += max(list_of_bids)
            break


def run_game():
    game_engine()
    bid_matching()
    print(f'The winner is {name_of_winner} with bid {winner_bid}$')

run_game()