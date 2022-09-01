# word = 'apple'  # Word to be guessed.
# user_word = '__ __ __ __ __'  # Word showing correct guesses of player so far.
# guess = ''  # Word inputted by player
# hint = 'Journey\'s Fruit from Heaven to Earth'  # Hint to word to be guessed.
# lives = 6


# # Introduces player to the rules of the game.
# def intro():
#     print(f'''
#         Welcome to the Hangman Game.\n
#         You try to guess a five-letter word correctly.\n
#         You have six lives.\n
#         You lose a life for every incorrect guess.\n
#         \n
#     ''')


# # Accepts user's input
# def accept_guess():
#     print(f'''
#         Word: {user_word}\n
#         Hint: {hint}\n
#         Lives: {lives}\n
#     ''')
#     guess = input('\tEnter a letter: ')
#     validate(guess)


# # Verification of length of input
# def validate(input):
#     while len(input) != 1:
#         input = input('\tEnter a single letter: ')

#     else:
#         guess = input
#         check_letter(input)


# # Check if letter is in word
# def check_letter(letter):
#     return letter in word


# # def incorrect_guess():
# #     print(f'''
# #             Incorrect guess!\n
# #             You have {lives} lifes left.\n
# #     ''')
# #     accept_guess()


# # Substitution of correct guesses into user_word
# def add_guess(word, user_word, letter):
#     index = word.index(letter)
#     word_list = user_word.split(' ')
#     word_list.pop(index)
#     word_list.insert(index, letter)
#     user_word = ' '.join(word_list)
#     return user_word


# intro()
# while lives > 0:
#     accept_guess()
#     if check_letter(guess):
#         add_guess(word, user_word, guess)

#     else:
#         lives -= 1
#         # incorrect_guess()


# else:
#     print('''
#         You have no lives left.
#         You have been hung!
#     ''')