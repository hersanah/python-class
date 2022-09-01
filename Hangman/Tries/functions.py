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
    print('You entered letter: ', guess)
    check_len(guess)


def check_len(user_input):
    while len(user_input) != 1:
        user_input = input('Enter a single letter: ')

    else:
        guess = user_input


def validate_guess(letter, word):
    if letter in word:
        return (letter, word.index(letter))
    else:
        return False

game_intro()
if exit == False:
    play_game()
    print(validate_guess(guess, word_to_guess))