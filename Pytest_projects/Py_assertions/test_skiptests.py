import sys

import pytest

pytestmark = pytest.mark.skipif(sys.platform == 'win32', reason="Will run only in linux ") # Skipped all tests inside the code
# test_skiptests.py::test_case0 SKIPPED (Will run only in linux)           [ 33%]
# Skipped: Will run only in linux
#
# test_skiptests.py::test_case1 SKIPPED (doesnot work on py version)       [ 66%]
# Skipped: doesnot work on py version
#
# test_skiptests.py::test_case2 SKIPPED (Will run only in linux)           [100%]
# Skipped: Will run only in linux

const = 9 / 5


def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah


# Print (cent_to_fah())

# def test_case0():
#     assert type(const) == float
#
#
# def test_case1():
#     assert cent_to_fah() == 32
#
#
# def test_case2():
#     assert cent_to_fah(38) == 100.4

# test_skiptests.py::test_case0 PASSED[33 %]
# test_skiptests.py::test_case1 PASSED[66 %]
# test_skiptests.py::test_case2 PASSED[100 %]

@pytest.mark.skip(reason="Skipping test for no reason specified")
def test_case0():
    assert type(const) == float


# test_skiptests.py::test_case0 SKIPPED (Skipping test for no reason specified)      [ 33%]
# Skipped: Skipping test for no reason specified

@pytest.mark.skipif(sys.version_info > (3,6), reason="doesnot work on py version")
def test_case1():
    assert cent_to_fah() == 32
# test_skiptests.py::test_case1 SKIPPED (doesnot work on py version)       [ 66%]
# Skipped: doesnot work on py version

def test_case2():
    assert cent_to_fah(38) == 100.4
