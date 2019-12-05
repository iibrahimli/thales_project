"""
A simple message used to pass information
between units.

"""

from util import *


class message:
    """
    Message passed from HMI to CPU to update 

    Attributes:
        e_type (int)   : Element type
        e_state (int)  : Element state
        elem (str)     : Subject that will be acted upon
        sender (str)   : Sender name

    """

    def __init__(self, e_type: int, e_state: int, elem: str, sender: str = None):
        self.e_type = e_type
        self.e_state = e_state
        self.elem = elem
        self.sender = sender