"""
This file contains different unit and integration tests
for the modules. If a module fails to pass a test

"""

from cpu import *
from gui import *
from sim import *
from util import *


def check_result(name, expected, calculated):
    """
    This function compares the result of a function to
    the provided reference result. Prints if failure is
    detected.

    Args:
        name (str) : Name of the test
        expected   : Expected result
        calculated : Calculated result

    """

    def print_test_failed():
        print(col.BOLD + f"{name}" + " -" + col.FAIL + " Test Failed" + col.ENDC, end="\n    ")
    
    def print_test_passed():
        print(col.BOLD + f"{name}" + " -" + col.OKGREEN + " Test Passed" + col.ENDC, end="\n")

    if type(expected) != type(calculated):
        print_test_failed()
        print(col.UNDERLINE + f"Type mismatch:" + col.ENDC + f" {type(expected)} != {type(calculated)}")
        print()
        return
    
    if expected != calculated:
        print_test_failed()
        print(col.UNDERLINE + f"Value mismatch:" + col.ENDC + f" {expected} != {calculated}")
        print()
        return
    
    print_test_passed()
    print()



"""
======================================================
             Start of the testing section             
======================================================
"""

# CPU



# SIM


check_result("Sample 1", 20.1, 1)
check_result("Sample 2", 120, 120)
check_result("Sample 3", 20.1, 10.1)