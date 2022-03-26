import random

world_list = []

with open('wordle-allowed-guesses.txt') as file:
    for line in file:
        world_list.append(line)
file.close()

answer = random.choice(world_list)

in_word = ''
not_in_word = ''
correct_letter = '_____'

def Check_answer(x):
    return x == answer

def Check_correct_positions(x):
    position = 0
    for letter in x:
        if x[position] == answer[position]:
            correct_letter[position] = letter
        if letter in answer:
            in_word.append(letter)
        if letter not in answer:
            not_in_word.append(letter)
        position += 1

def Check_valid_answer(x):
    return x == world_list

win = False
guess_count = 0
while guess_count <= 6 and Win is False:
    Guess = input('Enter first guess >> ')
    if Check_answer(Guess) is True:
        win = True
    else:
        Check_correct_positions(Guess)
    print('Correct letters so far:' + correct_letter)
    print('Letters in word:' + in_word)
    guess_count += 1
if win == True:
    print('You win.')
else:
    print('You Lose. Answer was ' + answer + '.')
