import pytest


# def test_cases():
#     # with pytest.raises(Exception):
#     #     assert (1/0)
#     with pytest.raises(ZeroDivisionError):
#         assert (1/0)
#         # assert 3 > 3
#
# def test_case2():
#     with pytest.raises(Exception) as excinfo:
#         assert (1,2,3) == (1,2,4)
#     print(str(excinfo))


def func1():
    raise ValueError("Exception func1 Raised")


def test_case2():
    with pytest.raises(Exception) as excinfo:
        # assert (1,2,3) == (1,2,4)
        func1()
    print(str(excinfo))
    assert (str(excinfo.value)) == "Exception func1 Raised"
