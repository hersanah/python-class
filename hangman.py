import random
from sre_parse import SPECIAL_CHARS

guess = ''
attempts = 0
SPECIAL_CHARS = '!@#$%^&*()_-+={\}[]|\\"\';:<>,.?/~`'


# ----------------------------------------------------------------------------------------------------

# Validation functions

# Validates a character to check if the character is a letter
def validate_letter(character):
    while True:
        while character in guessed_list:
            character = input(f'\n\'{character}\' has been guessed aleady; Enter another letter: ')

        if character == 'exit': break

        while character.isalpha() and len(character) != 1:
            error = {   character.isdigit(): '\nYou entered a number! Enter a letter instead: ',
                        character.isspace(): '\nNo spaces allowed! Enter a letter: ',
                        len(character) == 0: '\nYou have to give an input. Enter a letter: ',
                        len(character) > 1: '\nYou must have entered more than one character. Enter a single letter: ',
                        character in SPECIAL_CHARS: '\nError! You must have entered a special character. Enter a letter instead: '}
            
            for key in error:
                if key == True:
                    character = input(error[key])
            
        break
    return character


# Validates a character to check if it is a number and not more than a specified number in terms of length
def validate_number(character, length: int):
    while True:
        if character == 'exit': break

        if character.isdigit():
            while int(character) > length: 
                character = input(f'\nYou entered a number that is not on the category list. Enter a number between 1 and {length}: ')
                if character.isdigit() == False: break
        
        while (character.isdigit() and (len(character) == 1)) == False:
            error = {   character.isalpha(): '\nYou entered a letter! Enter a number instead: ',
                        character.isspace(): '\nNo spaces allowed! Enter a number: ',
                        len(character) == 0: '\nYou have to give an input. Enter a number: ',
                        len(character) > 1: '\nYou must have entered more than one character. Enter a single number: ',
                        character in SPECIAL_CHARS: '\nError! You must have entered a special character. Enter a number instead: '}
            
            for key in error:
                if key == True:
                    character = input(error[key])
            
        break
    return character
# ----------------------------------------------------------------------------------------------------


# Gives player introduction to the game and gets category player wants to play from.
def intro():
    print(f'''
    -------------------------------------------------------------------------------------------------
    Welcome to the Hangman Game.\n
    You try to guess a word correctly.\n
    You lose a life for every incorrect guess.\n
    --------------------------------------------------------------------------------------------------
    \n
    ''')

    category = validate_number(input('''
    Choose a category to select your word from among the categories below:
    1 - Disney Movies

    2 - Cities of the World

    3 - Foods

    4 - Fruits

    5 - Mammals

    Enter a number: 
    '''), 5)

    if category == 'exit': quit()

    return category


# ----------------------------------------------------------------------------------------------------

# Functions to return random words for different categories

# Returns category by number inputted by player form a dictionary of number-category form
def get_category(number):
    categories = {'1': get_d_movie, '2': get_city, '3': get_food, '4': get_fruit, '5': get_mammal}
    return categories[number]


# Returns a random movie from a list of movies
def get_d_movie():
    d_movies = {'Moana': 'sea-loving, headstrong, strong-willed, practically fearless, and physically capable',

                'Aladdin': 'poor yet care-free street urchin in an Arabian city',

                'Zootopia': 'city where animals live in harmony',

                'Pinocchio': 'acts like a human child; nose-growing lies',

                'Dumbo': 'baby elephant with extremely large ears who is capable of flying',

                'Enchanto': 'translates in English to charm or enchantment; family of magically powered characters',

                'Frozen': 'story on a journey to salvage a frozen kingdom in a fjord',

                'Bambi': 'fawn whose father is revered as the Great Prince of the Forest',

                'Tangled': 'story about a royal mess of long golden hair'}

    return random.choice(list(d_movies.items()))


# Returns a random city from a list of cities
def get_city():
    cities = {  'London': 'double-decker buses, red phone booths, world-class museums and an amusing eye',

                'Lagos': 'rich with yellow-and-black buses and traffic jams',

                'Oslo': 'norwegian city ruled by King Harald V',

                'Tokyo': 'place to realize knowledge or lack-thereof of anime',

                'Paris': 'city of love, gravity and a glass pyramid',

                'Istanbul': 'fascinating city built on two Continents',

                'Beijing': 'city to don your Qipao dress and Mandarin',

                'Amsterdam': 'city filled with beautiful canals, quirky architecture, rich history, Dutch art and the Red Light District',

                'Marrakech': 'red city of luxury, 5-star restaurants, luxury spas and hammams and charming riads',

                'Seoul': 'home to sleek skyscrapers and shopping malls, well-preserved royal palaces, Buddhist temples and Han River',

                'Madrid': 'home to some of Europe\'s finest collections of Spanish and Latin American art'}
    return random.choice(list(cities.items()))


# Returns a random food from a list of foods
def get_food():
    foods = {   'Donut': 'a small usually ring-shaped piece of sweet fried dough',

                'Ice Cream': 'a (usually) cone of ice-cold melting goodness',

                'Pizza': 'open-faced baked pie of Italian origin with radius \'z\' and thickness \'a\'',
                
                'Pasta': 'long strands of mixture of dough, flour and water',

                'Rice': 'edible starchy cereal grain and grass plant',

                'Chicken': 'meal made with a bird',

                'Turkey': 'meal made with a bird that shares name with a country',

                'Hamburger': 'food with fillings of patty placed inside a sliced bun',

                'Pancakes': 'pillows of goodness that get even better with syrup'}
    return random.choice(list(foods.items()))


# Returns a random fruit from a list of fruits
def get_fruit():
    fruits = {  'apple': 'red-green delicious mouth-watering fruit used to make pies',

                'pear': 'apple-looking fruits',

                'orange': 'of a color that is of the same name as the fruit',

                'mango': 'sweet stone fruit',

                'lemon': 'when life gives you it, you make a drink',

                'grape': 'berry fruit used for making wine, jam, juice, jelly, vinegar, or dried as raisins',

                'apricot': 'small, yellow, tart-tasting stone fruit',

                'guava': 'oval in shape with light green or yellow skin and contain edible seeds',

                'banana': 'elongated edible fruit; yellow when unripe and green when ripened',

                'pineapple': 'name with combination of names of a conifer tree and another sweet fruit'}
    return random.choice(list(fruits.items()))


# Returns a random animal from a list of animals
def get_mammal():
    mammals = { 'dog': 'man-friend',

                'cat': 'sassy and beautiful',

                'horse': 'gets you anywhere in no time',

                'donkey': 'load carrier',

                'cow': 'soaked in milk',

                'goat': 'human-like offspring',

                'lion': 'pride of the jungle',

                'snake': 'dangerous',

                'tiger': 'striped feline',

                'rabbit': 'ears at attention',

                'wolf': 'h-oooooooo-wl'}
    return random.choice(list(mammals.items()))


# Returns a random bird from a list of birds
def get_dessert():
    desserts = {'Brownies': '',
                'Ice-cream': '',
                'Cupcakes': '',
                'Cheesecake': '',
                '': '',
                'finch': '',
                'songbird': '',
                'owl': '',
                'mallard': ''}
    return random.choice(list(desserts.items()))
# ----------------------------------------------------------------------------------------------------


# Generates an asterisk-filled replica list of the word to be guessed
def list_star_gen(length):
    gen_list = []
    for i in range(length):
        gen_list.append('*')
    return gen_list


# Replaces an asterisk with the correct word at a random index
def get_hints(word):
    word_list = list_star_gen(len(word))
    index_list = []

    while True:
        to_show = random.randint(0, len(word)-1)

        if word.count(word[to_show]) == 1:
            word_list[to_show] = word[to_show]
            index_list.append(to_show)
            break

    if len(word) > 5:
        while True:
            while True:
                to_show = random.randint(0, len(word)-1)
                if word.count(word[to_show]) == 1:
                    break
            if to_show not in index_list:
                word_list[to_show] = word[to_show]
                break

    return ' '.join(word_list)


# When game is being exitted.
def exit_game():
    print(f'''
    You have exited the game.

    Letter(s) guessed so far: {' '.join(guessed_list)} after {attempts} attempts.
    ''')


(word_to_guess, hint) = get_category(intro())()
lives = len(word_to_guess)
show_some = get_hints(word_to_guess)
guessed_list = show_some.lower().split(' ')


def starting_details():
    print(f'''
    --------------------------------------------------------------------------------------------------
    Word: {' '.join(guessed_list)}

    Hint: {hint}

    Lives: {lives}

    Here are some of the letters shown: {show_some}

    To exit the game, enter \'exit\'.
    --------------------------------------------------------------------------------------------------
    ''')


def display_details():
    print(f'''
    --------------------------------------------------------------------------------------------------
    Word: {' '.join(guessed_list)}\n

    To exit the game, enter \'exit\'.
    --------------------------------------------------------------------------------------------------
    ''')


# Accepts guess from player as long as it is a one-letter word.
def get_guess():
    guess = validate_letter(input(f'''
    Enter a letter of your guess: 
    '''))

    return guess
    

# Finds all occurences of a letter in an iterable.
def find_all(iterable, item):
    temp = iterable.copy()
    index_es = []
    
    for i in range(iterable.count(item)):
        item_index = temp.index(item)
        index_es.append(item_index + i)
        temp.pop(item_index)
    return index_es


# Replaces all instances of a word in an iterable at indices of instances.
def replace_instances(iterable, indexes, letter):
    for index in indexes:
        iterable[index] = letter
    return iterable


# When player inputs a correct guess.
def correct_guess():
    print(f'''
    --------------------------------------------------------------------------------------------------
    {' '.join(guessed_list)}
    --------------------------------------------------------------------------------------------------
    ''')


# When player inputs an incorrect guess.
def incorrect_input():
    print(f'''
    --------------------------------------------------------------------------------------------------
    Incorrect Guess!

    {' '.join(guessed_list)}

    You have {lives} lives left.
    --------------------------------------------------------------------------------------------------
    ''')


# When a player has guessed all of the letters in the word.
def guess_complete():
    print(f'''
    Weldone! Thanks for Playing.

    You have guessed "{word_to_guess}" correctly after {attempts} attempts.

    You have come to the end of the game.
    --------------------------------------------------------------------------------------------------
    ''')


# When the player is out of lives.
def out_of_lives():
    print(f'''
    Oops! You are hanged!

    Correct Word: {word_to_guess}
    ''')


starting_details()

while lives > 0:
    display_details()

    guess = get_guess().lower()
    if guess == 'exit':
        exit_game()
        break
    attempts += 1

    if guess in list(word_to_guess.lower()):
        indices = find_all(list(word_to_guess.lower()), guess)

        guessed_list = replace_instances(guessed_list, indices, guess)

        correct_guess()

    else:
        lives -= 1

        incorrect_input()

    if ''.join(guessed_list) == word_to_guess.lower():
        guess_complete()

        break


else:
    out_of_lives()
