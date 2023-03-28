"""Main module."""

import random
import string

def generate_random_string(length, upper = False, digit = False, punc = False):
    """Generates a random string of a specified length."""
    chars = string.ascii_lowercase
    if upper:
        chars += string.ascii_uppercase
    if digit:
        chars += string.digits
    if punc:
        chars += string.punctuation
    
    result_str = ''.join(random.choice(chars) for i in range(length))
    return result_str

def generate_lucky_number(length = 1):
    result_str = ''.join(random.choice(string.digits) for i in range(length))
    result_str = int(result_str)
    return result_str
