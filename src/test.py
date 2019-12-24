"""
This file contains different unit and integration tests
for the modules. If a module fails to pass a test

"""

import inspect

from cpu import *
from simulator import *
from util import *


TEST_NAME_PAD_WIDTH = 50

n_tests = 0
n_passed = 0


def lineno():
    """
    Returns the current line number
    """
    return inspect.currentframe().f_back.f_back.f_lineno


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

    global n_tests, n_passed

    n_tests += 1

    def print_test_failed():
        print(col.BOLD + f"{name:{TEST_NAME_PAD_WIDTH}}" + " - " + col.FAIL + "Test Failed" + col.ENDC, end="\n    ")
    
    def print_test_passed():
        print(col.BOLD + f"{name:{TEST_NAME_PAD_WIDTH}}" + " - " + col.OKGREEN + "Test Passed" + col.ENDC, end="\n")

    if type(expected) != type(calculated):
        print_test_failed()
        print(col.UNDERLINE + f"Type mismatch:" + col.ENDC + f" {type(expected).__name__} != {type(calculated).__name__} (line {lineno()})")
        print()
        return
    
    if expected != calculated:
        print_test_failed()
        print(col.UNDERLINE + f"Value mismatch:" + col.ENDC + f" {expected} != {calculated} (line {lineno()})")
        print()
        return

    print_test_passed()
    print()
    n_passed += 1



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

m1 = message(SWITCHPOINT, 'Z3_1', PLUS)
m2 = message(SWITCHPOINT, 'Z3_1', PLUS)
m3 = message(SWITCHPOINT, 'Z2_1', PLUS)
check_result("CPU message equal", True, m1 == m2)
check_result("CPU message not equal", False, m1 == m3)

proc._reset()
proc.set_elem_state(ROUTE, 'A1-A3', OCCUPIED)
check_result("CPU set route state", OCCUPIED, proc.elements[ROUTE]['A1-A3'])

proc._reset()
check_result("CPU get uninitialized route state", None, proc.get_elem_state(ROUTE, 'A1-A3'))

proc._reset()
proc.set_elem_state(ROUTE, 'A1-A3', UNOCCUPIED)
check_result("CPU get initialized route state", UNOCCUPIED, proc.get_elem_state(ROUTE, 'A1-A3'))

proc._reset()
check_result("CPU check safety of a safe operation", True, proc.check_safety(SWITCHPOINT, 'Z3_1', RED))

proc._reset()
check_result("CPU check safety of a dangerous operation", False, proc.check_safety(SWITCHPOINT, 'Z3_1', GREEN))


# SIM module tests

print()
print(col.BOLD + col.HEADER + "SIM tests".center(TEST_NAME_PAD_WIDTH) + col.ENDC)
print(col.BOLD + col.HEADER + "="*TEST_NAME_PAD_WIDTH + col.ENDC)
print()

sml = simulator()

check_result("SIM sample check 1", 1, 1)

check_result("SIM sample check 2", 2, "2")

check_result("SIM sample check 3", 3, 3)


# print stats

print(col.BOLD + col.OKBLUE + "Stats".center(TEST_NAME_PAD_WIDTH))
print(col.BOLD + col.OKBLUE + "="*TEST_NAME_PAD_WIDTH + col.ENDC)
print()
print(col.BOLD +     "Total tests: " + col.ENDC + f"{n_tests}".rjust(TEST_NAME_PAD_WIDTH-13))
if n_passed == n_tests:
    print(col.BOLD + "Failed tests:" + col.ENDC + col.OKGREEN + f"{n_tests - n_passed} ({(n_tests - n_passed) / n_tests * 100:.1f} %)".rjust(TEST_NAME_PAD_WIDTH-13) + col.ENDC)
else:
    print(col.BOLD + "Failed tests:" + col.ENDC + col.FAIL + f"{n_tests - n_passed} ({(n_tests - n_passed) / n_tests * 100:.1f} %)".rjust(TEST_NAME_PAD_WIDTH-13) + col.ENDC)
