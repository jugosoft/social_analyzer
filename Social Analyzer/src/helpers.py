from random import randint
from time   import sleep
from enum   import Enum
import os

def delay():
    """
    Creates delay. We need it because of restrictions of Vk API.
    No more than 5 requests per second...
    """
    latency = 0.49
    sleep(latency)

class Colour(Enum):
    """
    Summary of class goes here.

    It makes matches between names of colours
    and their char expressions.

   Attributes:
       No any attributes yet.
    """
    RED             = 'r'
    GREEN           = 'g'
    BLUE            = 'b'
    YELLOW          = 'y'


clear = lambda: os.system('cls')