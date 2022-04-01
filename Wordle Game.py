import random

word_list = []

with open('wordle-allowed-guesses.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        word_list.append(line)
file.close()
with open('wordle-answers-alphabetical.txt') as file:
    for line in file:
        line = line.replace('\n', '')
        word_list.append(line)
file.close()

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

def Check_duplicate_letters(x):
    check_dup = []
    for letter in x:
            if letter not in check_dup:
                check_dup.append(letter)
                check_dup.sort()
    return check_dup

def Check_valid_guess(x):
    return x in word_list

play_again = True
while play_again == True:
    answer = random.choice(word_list)
    in_word = []
    not_in_word = []
    correct_letter = ['_','_','_','_','_']
    all_guesses = []
    win = False
    guess_count = 1
    while guess_count <= 6 and win == False:
        valid_guess = False
        while valid_guess == False:
            guess = input('Enter guess #'+ str(guess_count) + ' >> ')
            guess = guess.lower()
            if Check_valid_guess(guess):
                valid_guess = True
            else:
                print('Invalid guess. Guess again.')
        if Check_answer(guess):
            win = True
        else:
            Check_correct_positions(guess)
            in_word = Check_duplicate_letters(in_word)
            not_in_word = Check_duplicate_letters(not_in_word)
            all_guesses.append(guess)
            print()
            print('Guesses so far: '+ str(all_guesses).replace("'",'').replace(',',''))
            print('Correct letters so far:' + str(correct_letter).replace("'",'').replace(',',''))
            print('Letters in word:' + str(in_word).replace("'",'').replace(',',''))
            print('Letters not in word:' + str(not_in_word).replace("'",'').replace(',',''))

        guess_count += 1
    if win == True:
        print ('You win. Answer was ' + answer + '.')
    else:
        print ('You lose. Answer was ' + answer + '.')
    play_again_answer = input('Play again? >> ')
    if play_again_answer.lower() != 'y' and play_again_answer.lower() != 'yes':
        play_again = False
