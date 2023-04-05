"""Main module."""

import random
import string
import ipyleaflet


class Map(ipyleaflet.Map):

    def __init__(self, center, zoom, **kwargs):
        """_summary_

        Args:
            center (_type_): _description_
            zoom (_type_): _description_
        """        
        if 'scroll_wheel_zoom' not in kwargs:
            kwargs['scroll_wheel_zoom'] = True
        super().__init__(center = center, zoom = zoom, **kwargs) # inherited from the parent, in this case, ipyleaflet
    
    def add_search_control(self, position = 'topleft', **kwargs):
        """_summary_

        Args:
            position (str, optional): _description_. Defaults to 'topleft'.
        """        
        if 'url' not in kwargs:
            kwargs['url'] = 'https://nominatim.openstreetmap.org/search?format=json&q={s}'
        
        search_control = ipyleaflet.SearchControl(position = position, **kwargs)
        self.add_control(search_control)

    def add_draw_control(self, **kwargs):
        draw_control = ipyleaflet.DrawControl(**kwargs)
        self.add_control(draw_control)

    def add_layers_control(self, position = 'topright', **kwargs):
        """_summary_

        Args:
            position (str, optional): _description_. Defaults to 'topright'.
        """        
        layers_control = ipyleaflet.LayersControl(position = position, **kwargs)
        self.add_control(layers_control)



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
