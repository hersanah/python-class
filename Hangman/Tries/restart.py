# word = 'apple'  # Word to be guessed.
# user_word = '__ __ __ __ __'  # Word showing correct guesses of player so far.
# guess = ''  # Word inputted by player
# hint = 'Journey\'s Fruit from Heaven to Earth'  # Hint to word to be guessed.
# lives = 6


# print(f'''
#         Welcome to the Hangman Game.\n
#         You try to guess a five-letter word correctly.\n
#         You have six lives.\n
#         You lose a life for every incorrect guess.\n
#         \n
#     ''')

# while lives > 0:
#     print(f'''
#         Word: {user_word}\n
#         Hint: {hint}\n
#         Lives: {lives}\n
#     ''')
#     guess = input('\tEnter a letter: ')

#     if guess in word:
#         index = word.index(guess)
#         word_list = user_word.split(' ')
#         word_list.pop(index)
#         word_list.insert(index, guess)
#         user_word = ' '.join(word_list)
    

#     else:
#         lives -= 1
#         # incorrect_guess()


# else:
#     print('''
#         You have no lives left.
#         You have been hung!
#     ''')