import art
import string

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar():
    print(art.logo)
    game_switch = True
    while game_switch:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        processed_text = ''

        for i in text:
            if i not in string.ascii_lowercase:
                processed_text += i
                continue
            get_index = ALPHABET.index(i)
            if direction == 'encode':
                new_index = get_index + shift
                if new_index > 25:
                    new_index %= 26
                processed_text += ALPHABET[new_index]
            if direction == "decode":
                if shift > 26:
                    shift %= 26
                new_index = get_index - shift
                processed_text += ALPHABET[new_index]
        print(f'The {direction} text is {processed_text}.')
        game_repeat = input('Do you wanna start programme again? Enter Yes or No\n').lower()
        if game_repeat == 'no':
            print('Goodbye!')
            game_switch -= 1


caesar()
