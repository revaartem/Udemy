
with open("./Input/Names/invited_names.txt") as names:
    for name in names:
        with open(f'./Output/ReadyToSend/letter_for_{name.strip()}', "w") as letter:
            ready_letter = ''
            with open('Input/Letters/starting_letter.txt') as sample:
                for line in sample:
                    if '[name]' in line.strip():
                        ready_letter += line.replace('[name]', f'{name.strip()}')
                    else:
                        ready_letter += line

            letter.write(ready_letter)

