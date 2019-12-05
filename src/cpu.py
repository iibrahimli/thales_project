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
        """
        Initializes empty dicts
        
        """
        
        self.elements = {
            0: {},  # signals
            1: {}   # switchpoints
        }

    
    def _reset(self):
        """
        Resets the state of the CPU

        """

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


    def set_elem_state(self, e_type, elem, e_state):
        """
        Get the state of a given element

        Arguments:
            e_type (int)  : Element type
            elem (str)    : Element name
            e_state (int) : Element state

        """

        self.elements[e_type][elem] = e_state


    def recv_message(self, m):
        """
        Receive and parse a message

        Arguments:
            m (message) : The message

        """

        self.set_elem_state(m.e_type, m.elem, m.e_state)
    

    def check_safety(self, e_type, elem, e_state):
        """
        Check the safety of an operation

        Arguments:
            e_type (int)  : Element type
            elem (str)    : Element name
            e_state (int) : Element state

        Returns:
            safe (bool) : True if the operation is safe, False otherwise    

        """

        return False