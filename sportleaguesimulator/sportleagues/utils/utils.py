'''
Utilities functions
'''
import string
import random

def print_list(list):
    for item in list:
        print(item)

# Return a random uppercase letter
def generate_random_letter():
    return random.choice(string.ascii_letters).upper()

def generate_random_jersey_number():
    return random.randint(0, 100)
