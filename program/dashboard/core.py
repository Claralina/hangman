import pandas as pd
import numpy as np
import random
from visualize import *

path = '../static_files/'


def get_choose_word():
    word_list = open(path + 'words.txt', 'r').read().split('\n')
    word = (np.random.choice(word_list, 1))[0].lower()
    print(word)
    return word


def get_guess(g):
    guess = g.lower()
    return guess


def check_guess(word, guess):
    if guess not in word:
        print('false')
        count_fails()
    else:
        print('true')
        print('congrats you found one letter')


def count_fails():
    fail_counter = + 1
    return fail_counter


def check_for_max_fails(fail_counter, MAX_FAILS):
    if fail_counter == MAX_FAILS:
        more_tries = False
    return more_tries


def start_game():
    MAX_FAILS = 5
    more_tries = True

    word = get_choose_word()
    while more_tries:
        guess = get_guess()
        fail_counter = check_guess(word, guess)
        check_for_max_fails(fail_counter, MAX_FAILS)
