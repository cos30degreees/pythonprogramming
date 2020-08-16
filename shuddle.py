# 1) Write a function that takes a string as an input and returns a shuffled version of that string
# (i.e. a version where each character is just as likely to be in any given position)
import random

from collections import Counter
def shuffle_word(input_word):
    shuffled_word = {}
    shuffled_words = []
    for char in input_word:
        index = random.randint(0,len(input_word)-1)
        while index in shuffled_word.keys():
            index = random.randint(0,len(input_word)-1)
        shuffled_word[index] = char
    for k,v in shuffled_word.items():
        shuffled_words.insert(k,v)
    return ''.join(shuffled_words)

not_shuffled = 'hello my name is '
shuffled = shuffle_word(not_shuffled)


def same_structure(str1,str2):
    same_char = []
    different_char =[]
    for index,char in enumerate(str1):
        if str2[index] == char:
            same_char.append((index,char))
        else:
            different_char.append([index,str1[index],str2[index]])
    print('Same letters Location {}'.format(same_char))
    print('different letters found at this location {}:'.format(different_char))


def get_letter_count(str1,str2):
    str1_letter_counter = Counter(str1)
    str2_letter_counter = Counter(str2)
    print(str2_letter_counter)
    print(str1_letter_counter)



same_structure(not_shuffled,shuffled)
get_letter_count(not_shuffled,shuffled)
