"""
Central Processing Unit

"""

from util import *
from message import *


class cpu:
    """
    Central processing unit for the station interlocking system

    Attributes:
        switchpoints (dict) : Element name (str) -> state (int)
        signals (dict)      : Element name (str) -> state (int)

    """

    def __init__(self):
        self.elements = {
            0: {},  # signals
            1: {}   # switchpoints
        }
    

    def get_elem_state(self, e_type, elem):
        """
        Get the state of a given element

        Arguments:
            e_type (int)  : Element type
            elem (str)    : Element name

        Returns:
            e_state (int) : Element state

        """

        return self.elements[e_type].get(elem, None)


    def recv_message(self, m: message):
        """
        Receive and parse message

        Arguments:
            m (message) : The message

        """

        self.elements[m.e_type][m.elem] = m.e_state