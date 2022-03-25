import random

world_list = []
with open('wordle-allowed-guesses.txt') as file:
    for line in file:
        world_list.append(line)
file.close()

answer = random.choice(world_list)

in_word = []
correct_letter = '_____'

def Check_answer(x):
    return x == answer

def Check_correct_positions(x):
    position = 0
    for letter in x:
        if letter in answer:
            in_word.append(letter)
        if x[position] == answer[position]:
            correct_letter[position] = letter
        position += 1
    in_word_checked = []
    for letter in in_word:
        if letter not in in_word:
            in_word_checked.append(letter)
    in_word = in_word_checked


Guess1 = input('Enter first guess >> ')
if Check_answer(Guess1) == True:
    print ('You win!')

Check_correct_positions(Guess1)

Guess2 = input('Enter first guess >> ')

Guess3 = input('Enter first guess >> ')

Guess4 = input('Enter first guess >> ')

Guess5 = input('Enter first guess >> ')

Guess6 = ('Enter first guess >> ')

