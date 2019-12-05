"""
This file contains different unit and integration tests
for the modules. If a module fails to pass a test

"""

from cpu import *
from gui import *
from sim import *
from util import *


TEST_NAME_PAD_WIDTH = 32


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
        print(col.BOLD + f"{name:{TEST_NAME_PAD_WIDTH}}" + " - " + col.FAIL + "Test Failed" + col.ENDC, end="\n    ")
    
    def print_test_passed():
        print(col.BOLD + f"{name:{TEST_NAME_PAD_WIDTH}}" + " - " + col.OKGREEN + "Test Passed" + col.ENDC, end="\n")

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


# CPU module tests

print(col.BOLD + col.HEADER + "CPU tests".center(TEST_NAME_PAD_WIDTH) + col.ENDC)
print(col.BOLD + col.HEADER + "="*TEST_NAME_PAD_WIDTH + col.ENDC)
print()

proc = cpu()

proc.set_elem_state(SIGNAL, 'A1_4', GREEN)
check_result("CPU set uninitialized element", GREEN, proc.elements[SIGNAL]['A1_4'])

proc._reset()
proc.set_elem_state(SIGNAL, 'A1_4', RED)
proc.set_elem_state(SIGNAL, 'A1_4', GREEN)
check_result("CPU set initialized element", GREEN, proc.elements[SIGNAL]['A1_4'])

proc._reset()
check_result("CPU get uninitialized element", None, proc.get_elem_state(SIGNAL, 'A1_4'))

proc._reset()
proc.set_elem_state(SIGNAL, 'A1_4', GREEN)
check_result("CPU get initialized element", GREEN, proc.get_elem_state(SIGNAL, 'A1_4'))

proc._reset()
proc.set_elem_state(SIGNAL, 'A1_4', RED)
proc._reset()
check_result("CPU reset", None, proc.get_elem_state(SIGNAL, 'A1_4'))

proc._reset()
m = message(SWITCHPOINT, 'Z3_1', PLUS)
proc.recv_message(m)
check_result("CPU receive message", PLUS, proc.get_elem_state(SWITCHPOINT, 'Z3_1'))



# Simulator module tests
