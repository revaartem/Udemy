import random
import hanfman_art
import hangman_words

print(hanfman_art.logo)
word_list = ['hakoona', 'matata', 'renault']
choosen_word = random.choice(hangman_words.word_list)
deadmen_counter = 6
entered_letters = []

display = []
stages = hanfman_art.stages

for _ in range(len(choosen_word)):
    display.append('_')

end_of_game = False

while not end_of_game:
    guess = input('Enter letter: ').lower()
    if guess not in entered_letters:
        entered_letters.append(guess)
    else:
        print(f'You already entered this letter! Try another one.')
        continue
    for index, char in enumerate(choosen_word):
        if guess in choosen_word:
            if char == guess:
                display[index] = guess
    if guess not in choosen_word:
        deadmen_counter -= 1
        print(f'"{guess.capitalize()}" not in this word, and you lose a 1 life. Try another one.')

    print(f'Entered letters - {entered_letters}')
    print(display)
    print(stages[deadmen_counter])
    print('#' * 60)
    print('#' * 60)
    if not deadmen_counter:
        print('You lose!')
        end_of_game = True
    if '_' not in display:
        end_of_game = True
if deadmen_counter:
    print("You win!")