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
        
        self._reset()
       
        # switchpoints 
        self.elements[SWITCHPOINT]['2a']=""
        self.elements[SWITCHPOINT]['1a']=""
        self.elements[SWITCHPOINT]['1']=""
        self.elements[SWITCHPOINT]['2']=""
        self.current_route = ""

        # signals
        self.elements[SIGNAL]['A1_3']=""
        self.elements[SIGNAL]['A2_3']=""
        self.elements[SIGNAL]['A2_4']=""
        self.elements[SIGNAL]['E1_z2']=""
        self.elements[SIGNAL]['E1_z1']=""
        self.elements[SIGNAL]['E2_z2']=""

        #routes
        self.elements[ROUTE]['A1 A3']=""
        self.elements[ROUTE]['A2 A3']=""
        self.elements[ROUTE]['A2 A4']=""
        self.elements[ROUTE]['E1 z2']=""
        self.elements[ROUTE]['E1 z1']=""
        self.elements[ROUTE]['E2 z2']=""

    
    def _reset(self):
        """
        Resets the state of the CPU

        """

        self.elements = {
            SIGNAL:      {},   # signals
            SWITCHPOINT: {},   # switchpoints
            SECTION:     {},   # sections
            ROUTE:       {}    # routes
        }
        self.current_route = ""
    

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
        if e_type == ROUTE:
            if e_state == SET:
                self.current_route = elem
            else:
                self.current_route = ""


    def recv_message(self, m):
        """
        Receive and parse a message

        Arguments:
            m (message) : The message

        """

        self.set_elem_state(m.e_type, m.elem, m.e_state)
    

    def check_safety(self, e_type, elem, e_state):
        """
      Check the safety of an operation with the
      control table.

      Arguments:
            e_type (int)  : Element type
            elem (str)    : Element name
            e_state (int) : Element state

        Returns:
            safe (bool) : True if the operation is safe, False otherwise

        """
        # checking signal safety
        if message(e_type, elem, e_state) == message(SIGNAL, 'A1_3', GREEN)  or \
           message(e_type, elem, e_state) == message(SIGNAL, 'A2_3', GREEN)  or \
           message(e_type, elem, e_state) == message(SIGNAL, 'A2_4', GREEN)  or \
           message(e_type, elem, e_state) == message(SIGNAL, 'E1_z2', GREEN) or \
           message(e_type, elem, e_state) == message(SIGNAL, 'E1_z1', GREEN) or \
           message(e_type, elem, e_state) == message(SIGNAL, 'E2_z2', GREEN):
            return True

        # checking route safety
        elif message(e_type, elem, e_state) == message(ROUTE, 'A1 A3', SET):
           if self.elements[SWITCHPOINT]['1a'] == PLUS:
            return True
           else:
            return False
        elif message(e_type, elem, e_state) == message(ROUTE, 'A2 A3', SET):
           if self.elements[SWITCHPOINT]['2a'] == PLUS and self.elements[SWITCHPOINT]['1a'] == MINUS:
            return True
           else:
            return False
        elif message(e_type, elem, e_state) == message(ROUTE, 'A2 A4', SET):
           if self.elements[SWITCHPOINT]['2a'] == PLUS:
            return True
           else:
            return False
        elif message(e_type, elem, e_state) == message(ROUTE, 'E1 z2', SET):
           if self.elements[SWITCHPOINT]['1'] == PLUS and self.elements[SWITCHPOINT]['1a'] == MINUS and self.elements[SWITCHPOINT]['2a'] == MINUS:
            return True
           else:
            return False
        elif message(e_type, elem, e_state) == message(ROUTE, 'E1 z1', SET):
           if self.elements[SWITCHPOINT]['1'] == PLUS and self.elements[SWITCHPOINT]['1a'] == PLUS:
            return True
           else:
            return False
        elif message(e_type, elem, e_state) == message(ROUTE, 'E2 z2', SET):
           if self.elements[SWITCHPOINT]['2a'] == PLUS:
            return True
           else:
            return False

        # nothing above matched
        else:
            return False