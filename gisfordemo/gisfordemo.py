"""Main module."""

import random
import string

def generate_random_string(length, upper = False, digit = False, punc = False):
    """Generates a random string of a given length.

    Args:
        length (int): _description_
        upper (bool, optional): _description_. Defaults to False.
        digit (bool, optional): _description_. Defaults to False.
        punc (bool, optional): _description_. Defaults to False.

    Returns:
        str: _description_
    """
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
    """_summary_

    Args:
        length (int, optional): _description_. Defaults to 1.

    Returns:
        int: _description_
    """    
    result_str = ''.join(random.choice(string.digits) for i in range(length))
    result_str = int(result_str)
    return result_str
