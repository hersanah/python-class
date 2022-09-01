word_to_guess = 'apple'  # Word to be guessed.
user_word = '__ __ __ __ __'  # Word showing correct guesses of player so far.
guess = ''  # Word inputted by player
hint = 'Journey\'s Fruit from Heaven to Earth'  # Hint to word to be guessed.
lives = 6
exit = False


def game_intro():
    print(f'''
    Welcome to the Hangman Game.\n
    You try to guess a five-letter word correctly.\n
    You have six lives.\n
    You lose a life for every incorrect guess.\n
    \n
    ''')


def play_game():
    print(f'''
    Word: {user_word}\n
    Hint: {hint}\n
    Lives: {lives}\n
    ''')
    guess = input('Enter a letter: ')
    check_len(guess)


def check_len(user_input):
    while len(user_input) != 1:
        user_input = input('Enter a single letter: ')

    else:
        guess = user_input


def validate_guess(letter, word):
    if letter in word:
        return (guess, word.index(guess))
    else:
        return False


def include_letter(letter, word):
    index = validate_guess(letter, word)[1]
    word_list = word.split(' ')
    word_list.pop(index)
    word_list.insert(index, letter)
    word = ' '.join(word_list)
    return word


def incorrect_guess():
    print(f'''
            Incorrect guess!\n
            You have {lives} lifes left.\n
            \n
            Try Again!\n
    ''')
    play_game()


game_intro()
while lives > 0:
    if exit == False:
        play_game()
        validate_guess(guess, word_to_guess)

        if validate_guess(guess, word_to_guess) == False:
            lives -= 1
            incorrect_guess()

        else:
            print('''
                Correct Guess!
            ''')        
            print(include_letter(guess, user_word))

    else:
        print('You have ended the game')
        break

else:
    print('You have been hanged!')