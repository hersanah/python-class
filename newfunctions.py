word_to_guess = 'bagel'
lives = 9
exit = False
guessed_list = ['*', '*', '*', '*', '*']
guess = ''
hint = 'Roundo in a bag'  # Hint to word to be guessed.


def game_intro():
    print(f'''
    Welcome to the Hangman Game.\n
    You try to guess a five-letter word correctly.\n
    You have six lives.\n
    You lose a life for every incorrect guess.\n
    \n
    ''')


def accept_input():
    print(f'''
    Word: {' '.join(guessed_list)}\n
    Hint: {hint}\n
    Lives: {lives}\n
    ''')

    while True:
        guess = input('    Enter a single letter: ').lower()
        if len(guess) == 1: break
    print('\n    You entered letter: ', guess)
    return guess


def in_word():
    guess = accept_input()
    return guess in list(word_to_guess)


def letter_to_list(guessed_list):
    guess = accept_input()
    letter_index = list(word_to_guess).index(guess)
    guessed_list[letter_index] = guess
    return (guessed_list())


def hangman():
    game_intro()
    accept_input()
    print(letter_to_list(guessed_list))
    # if in_word():
    #     letter_to_list()
    #     print(f'''
    #         Correct Guess!
    #         {''.join(letter_to_list())}
    #         You have {letter_to_list().count('*')} letters left.
    #     ''')
    # else:
    #     lives -= 1
    #     print(f'''
    #         Incorrect Guess!
    #         {''.join(letter_to_list)}
    #         You have {lives} left.
    #     ''')


hangman()