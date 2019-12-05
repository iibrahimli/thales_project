"""
This file contains utility functions such as 
color printing, etc

"""


class col:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'


SIGNAL_RED        = 0
SIGNAL_GREEN      = 1
SWITCHPOINT_PLUS  = 2
SWITCHPOINT_MINUS = 3