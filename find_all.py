import random

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


def list_star_gen(length):
    gen_list = []
    for i in range(length):
        gen_list.append('*')
    return gen_list


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

word = list('apple')
# print(find_all(list('apple'), 'p'))
indexes = find_all(word, 'p')

shown = print(get_hints('appppppy'))
