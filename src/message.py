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
        elem (str)     : Subject that will be acted upon
        e_state (int)  : Element state
        sender (str)   : Sender name

    """

    def __init__(self, e_type, elem, e_state, sender=None):
        self.e_type = e_type
        self.elem = elem
        self.e_state = e_state
        self.sender = sender