word_to_guess = 'apple'
lives = 6
exit = False
guessed = '__ __ __ __ __'
guess = ''
hint = 'Journey\'s Fruit from Heaven to Earth'  # Hint to word to be guessed.


def game_intro():
    print('''
    Welcome to the Hangman Game.\n
    You try to guess a five-letter word correctly.\n
    You have six lives.\n
    You lose a life for every incorrect guess.\n
    \n
    ''')


def play_game():
    print(f'''
    Word: {guessed}\n
    Hint: {hint}\n
    Lives: {lives}\n
    ''')
    guess = input('Enter a letter: ')
    print('You entered letter: ', guess)


def check_len(word):
    while len(word) != 1:
        word = input('Enter a single letter: ')

    else:
        guess = word
        print('Great! You entered a one-letter word')


game_intro()
play_game()
check_len(guess)