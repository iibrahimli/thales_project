"""
This file contains utility functions such as 
color printing, etc

"""

# debug mode
DEBUG = True

class col:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'


# the type of the field element
SIGNAL        = 0
SWITCHPOINT   = 1

# state
MINUS    = 0
PLUS     = 1

# state
RED      = 0
GREEN    = 1